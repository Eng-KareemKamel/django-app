from django.urls import path
from .views import create_order, order_success

urlpatterns = [
    path('new/', create_order, name='order_create'),
    path('success/', order_success, name='order_success'),
]