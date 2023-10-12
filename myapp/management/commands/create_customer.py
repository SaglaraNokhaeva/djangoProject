from django.core.management.base import BaseCommand
from myapp.models import Сustomer


class Command(BaseCommand):
    help = "Create customer."
    def handle(self, *args, **kwargs):
        # customer = Сustomer(name='John', email='john@example.com',
        # phone='9999999999', adr='hdfjs hfjsf hfjkksdhf', date = '2025-09-09')
        customer = Сustomer(name='Peter', email='peter@example.com',
                            phone='8888888888', adr='jhgjhgj hjhgjsdhf', date='2023-09-09')
        customer.save()
        self.stdout.write(f'{customer}')
