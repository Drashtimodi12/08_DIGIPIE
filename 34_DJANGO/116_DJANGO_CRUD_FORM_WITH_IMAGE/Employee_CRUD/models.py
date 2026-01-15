from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to="EmpProfile/", null=True)

    def __str__(self):
        return f"{self.name} | {self.department} | {self.age} | {self.phone} | {self.email} "
