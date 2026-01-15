from django.db import models

# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    salary = models.FloatField()
    department = models.CharField(max_length=100)