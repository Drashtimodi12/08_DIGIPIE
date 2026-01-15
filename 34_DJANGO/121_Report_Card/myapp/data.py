# link: https://www.geeksforgeeks.org/python/python-faker-library/

from faker import Faker
fake = Faker()
import random
from myapp.models import *

def generate(n=50):
    for i in range(n):
        alldept = Department.objects.all()
        dept = alldept[random.randint(0, len(alldept)-1)]
        name = fake.name()
        email = fake.email()
        age = fake.random_int(18,25)
        stid = f"STD_{random.randint(100,999)}"
        studentid = StudentID.objects.create(stid=stid)
        Student.objects.create(dept=dept, stid=studentid, name=name, email=email, age=age)
        # print(name, email, age, dept, studentid)

def setMarks():
    allstudent = Student.objects.all()
    for student in allstudent:
        allsubject = Subject.objects.all()
        for subject in allsubject:
            Marks.objects.create(student=student, subject=subject, marks=random.randint(0, 100))