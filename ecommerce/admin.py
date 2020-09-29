from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, DeliveryAddress


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)
