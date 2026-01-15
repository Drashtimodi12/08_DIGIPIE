import random       # For generating random numbers (used for age)
import string       # For generating random strings (not used in this example)
from faker import Faker     # Faker library to generate fake realistic data
from myapp.models import *  # Importing all models from myapp.models
fake = Faker()      # Create a Faker instance

# Loop to create and insert 10 fake student records
for i in range(10):         
    username = fake.name()      # Generate a fake username (full name)
    email = fake.email()        # Generate a fake email address
    phone = fake.phone_number() # Generate a fake phone number
    age = random.randint(15,25) # Generate a random age between 15 and 25
    # print(username, email, phone, age)    # Create a new Student object and save it to the database   


    # Insert the generated data into the Student table using Django ORM
    Student.objects.create(
        username = username,    # Full name as username
        email = email,      # Email address
        phone = phone,      # Phone number
        age = age       # Age as a random integer
    )