from django.core.management.base import BaseCommand
from myapp.models import Сustomer


class Command(BaseCommand):
    help = "Create customer."
    def handle(self, *args, **kwargs):
        customer = Сustomer(name='John', email='john@example.com',
        phone='9999999999', adr='hdfjs hfjsf hfjkksdhf', date = '2025-09-09')
        customer.save()
        self.stdout.write(f'{customer}')
