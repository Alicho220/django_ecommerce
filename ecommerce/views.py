from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import *

from django.http import JsonResponse


def store(request):
    product = Product.objects.all()
    context={"products":product}
    return render(request, "ecommerce/store.html", context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context={"products":product}
    return render(request, "ecommerce/detail", context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items':items, 'order': order}
    return render(request, "ecommerce/cart.html",context)
   


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items':items, 'order': order}
    return render(request, "ecommerce/checkout.html", context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False
    )