from django.core.management.base import BaseCommand
from myapp.models import Order, Сustomer


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Сustomer ID')
    def handle(self, *args, **kwargs):
        # customer = models.ForeignKey(Сustomer, on_delete=models.CASCADE)
        # products = models.ManyToManyField(Product)
        # amount = models.DecimalField(max_digits=8, decimal_places=2)
        # date = models.DateTimeField(auto_now_add=True)

        # customer = Сustomer(name='John', email='john@example.com',
        # phone='9999999999', adr='hdfjs hfjsf hfjkksdhf', date = '2025-09-09')
        order = Order(customer=customer, products='Name1',
                            amount='123456.58', date='2023-09-09')
        order.save()
        self.stdout.write(f'{order}')