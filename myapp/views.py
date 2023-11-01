from django.shortcuts import render, get_object_or_404
from .models import Сustomer, Product, Order

# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторятся.
def customer_orders(request, customer_id):
    customer = get_object_or_404(Сustomer, pk = customer_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author':
    author, 'posts': posts})

# Create your views here.
