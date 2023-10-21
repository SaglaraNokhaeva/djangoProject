from django.core.management.base import BaseCommand
from myapp.models import Order, Сustomer, Product


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('id_customer', type=int, help='Сustomer ID')
        parser.add_argument('-p', '--Product_id', nargs='+', help="customer ID", required=True)
    def handle(self, *args, **kwargs):
        id_customer = kwargs.get('id_customer')
        Product_id: list = kwargs.get('Product_id')
        customer = Сustomer.objects.filter(pk=id_customer).first()

        order = Order(customer=customer)
        total_price = 0
        for i in range(0, len(Product_id)):
            product = Product.objects.filter(pk=Product_id[i]).first()
            total_price += float(product.price)
            order.amount = total_price
            order.save()
            order.products.add(product)

        # customer = Сustomer.objects.get(id=id_customer)
        # products = Сustomer.objects.get(id=id_product)
        # order = Order(customer=customer, products=products,
        #                     amount='123456.58', date='2023-09-09')
        # order.save()
        # self.stdout.write(f'{order}')