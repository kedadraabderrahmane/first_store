from django.db import models
from django.contrib.auth.models import User
import requests 
from bs4 import BeautifulSoup
# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    image=models.ImageField(upload_to='photos')
    describtion=models.TextField()
    def __str__(self):
        return self.name
class CartItem(models.Model):
  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'



class Wilaya(models.Model):
        
        
        # wilayat_tuple=[(wilaya,wilaya) for wilaya in wilayat]
        name=models.CharField(max_length=20)
        def __str__(self):
            return self.name


class Commune(models.Model):
    
    name=models.CharField(max_length=20)
    wilaya=models.ForeignKey(Wilaya,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Orders(models.Model):
   
    fullname=models.CharField(max_length=20)
    numero=models.IntegerField()
    wilaya=models.ForeignKey(Wilaya,on_delete=models.CASCADE)
    commune=models.ForeignKey(Commune,on_delete=models.CASCADE)




