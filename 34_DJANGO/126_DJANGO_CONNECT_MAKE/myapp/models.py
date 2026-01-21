from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.username} | {self.email} | {self.phone} | {self.age}"