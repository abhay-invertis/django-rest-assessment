from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
    return self.name