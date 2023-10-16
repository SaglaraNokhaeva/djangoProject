from random import random, randint

from django.core.management.base import BaseCommand
from myapp.models import Product
class Command(BaseCommand):
    help = ("Generate fake products.")
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}', description = f'description about product{i}', price=f'{randint(100000, 999999)}.{randint(0, 99)}', count = f'{randint(0, 100)}', date=f'2023-10-16')
            product.save()

