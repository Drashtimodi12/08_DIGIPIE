from myapp.models import *
import random
import string
from faker import Faker
fake = Faker()

print("\nStudent Data: \n")
for i in range(1, 21):
    username = fake.name()
    email= fake.email()
    phone =fake.msisdn()[:10]
    age = random.randint(18,30)
    print(username, email, phone, age)

    Student.objects.create(
        username=username,
        email=email,
        phone=phone,
        age=age
    )
   
    
print("\nEmployee Data: \n")
for i in range(20):
    name = fake.name()
    department = random.choice(["HR", "IT", "Finance", "Marketing"])
    email = fake.email()
    phone = fake.msisdn()[:10]
    age = random.randint(22, 50)
    print(name, department, email, phone, age)
    
    Employee.objects.create(
        name=name,
        department=department,
        email=email,
        phone=phone,
        age=age
    )