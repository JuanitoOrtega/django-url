from django.conf import settings
from django.db import models
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super().all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        # print(items)
        qs = ShortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return  'New codes made: {i}'.format(i=new_codes)


# Create your models here.
class ShortURL(models.Model):
    url = models.CharField(max_length=220, verbose_name='URL')
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True, verbose_name='Shortcode')
    updated_at = models.DateTimeField(auto_now=True) # Cada vez que el modelo es guardado
    created_at = models.DateTimeField(auto_now_add=True) # Cuando se crea el modelo
    active = models.BooleanField(default=True)

    objects = ShortURLManager()
    # some_random = ShortURLManager()

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

    def save(self, *args, **kwargs):
        # print('Saved something')
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url