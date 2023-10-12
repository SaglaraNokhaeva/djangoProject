from django.core.management.base import BaseCommand
from myapp.models import Сustomer
class Command(BaseCommand):
    help = "Get customer by id."
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        id = kwargs['id']
        customer = Сustomer.objects.get(id=id)
        self.stdout.write(f'{customer}')