from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    country  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} | {self.country}"
        

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} | {self.price} | {self.published_year} | {self.author.name}"
