from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

def __str__(self):
    return f"{self.name} - ({self.email})"



class Product(models.Model):
    name = models.CharField(max_length= 100)
    price = models.DecimalField(decimal_places=2 ,max_digits=8)

def __str__(self):
    return f"{self.name} - ₹{self.price}"



class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)    
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)



def __str__(self):
    return f"Order #{self.id} - {self.customer.name} - ₹{self.total_amount}"
