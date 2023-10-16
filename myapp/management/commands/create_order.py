from django.core.management.base import BaseCommand
from myapp.models import Order, Сustomer


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('id_customer', type=int, help='Сustomer ID')
        parser.add_argument('id_product', type=int, help='product ID')
    def handle(self, *args, **kwargs):

        # customer = Сustomer(name='John', email='john@example.com',
        # phone='9999999999', adr='hdfjs hfjsf hfjkksdhf', date = '2025-09-09')
        id_customer = kwargs['id_customer']
        id_product = kwargs['id_product']
        customer = Сustomer.objects.get(id=id_customer)
        products = Сustomer.objects.get(id=id_product)
        order = Order(customer=customer, products=products,
                            amount='123456.58', date='2023-09-09')
        order.save()
        self.stdout.write(f'{order}')