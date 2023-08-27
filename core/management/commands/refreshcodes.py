from django.core.management.base import BaseCommand, CommandError
from core.models import ShortURL


class Command(BaseCommand):
    help = "Refresh all ShortURL shortcodes"

    def add_arguments(self, parser):
        parser.add_argument("items", type=int) # python manage.py refreshcodes 10
        # parser.add_argument("number1", type=int)
        # parser.add_argument("number2", type=int)

    def handle(self, *args, **options):
        # print(options)
        return ShortURL.objects.refresh_shortcodes(items=options['items']) # python manage.py refreshcodes