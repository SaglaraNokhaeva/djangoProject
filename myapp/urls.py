from django.urls import path
from .views import customer_orders, order_full
urlpatterns = [
    path('customer_orders/<int:customer_id>/', customer_orders, name='customer_orders'),
    path('order_full/<int:order_id>/', order_full, name='order_full'),
]
