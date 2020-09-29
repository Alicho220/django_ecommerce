from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, null=True,)
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    item_name= models.CharField(max_length=200)
    price= models.FloatField(null=True, blank=True)
    image= models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False, null= True, blank= False)

    def __str__(self):
        return self.item_name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.transaction_id



class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now=True)



class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    address = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=100, null = True)
    state = models.CharField(max_length=100, null = True)
    date_added = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.address

