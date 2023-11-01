from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from .models import Сustomer, Product, Order

# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторятся.
def customer_orders(request, customer_id, is_Present=None):
    today = date.today()
    seven_day_before = today - timedelta(days=7)
    # present_employees_all = is_Present.objects.filter(date__gte=seven_day_before, is_present=True)
    # seven_day_before = today - timedelta(days=7)
    # present_employees_all = is_Present.objects.filter(date__gte=seven_day_before, is_present=True)
    products = []
    customer = get_object_or_404(Сustomer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    # for x in range(len(products)):
    #     print(products[x])
    return render(request, 'myapp/customer_orders.html', {'customer': customer, 'orders': orders, 'products': products})

# today = date.today()
# seven_day_before = today - timedelta(days=7)
# present_employees_all = is_Present.objects.filter(date__gte=seven_day_before, is_present=True)


def order_full(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'myapp/order_full.html', {'order': order})
# Create your views here.
