from django.core.management.base import BaseCommand
from myapp.models import Сustomer
class Command(BaseCommand):
    help = "Get all Сustomers."
    def handle(self, *args, **kwargs):
        customers = Сustomer.objects.all()
        self.stdout.write(f'{customers}')