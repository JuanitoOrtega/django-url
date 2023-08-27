from django.contrib import admin
from .models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortcode', 'active']
    list_editable = ['active']


admin.site.register(ShortURL, ShortURLAdmin)