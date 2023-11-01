from django.urls import path
from .views import customer_orders
urlpatterns = [
    path('customer_orders/<int: customer_id>/', customer_orders, name='customer_orders'),
]
