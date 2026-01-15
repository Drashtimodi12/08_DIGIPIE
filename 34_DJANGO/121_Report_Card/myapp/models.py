from django.db import models


# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100)

# we use to show all the data in admin panel
    def __str__(self):
        return self.name

class StudentID(models.Model):
    stid = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.stid
    
class Student(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    stid = models.ForeignKey(StudentID, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()

    # def __str__(self):
    #     return f"{self.name} | {self.email} | Age: {self.age} | Dept: {self.dept.name} | ID: {self.stid.stid}"

    
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    # def __str__(self):
    #     return f"{self.student.name} | {self.subject.name} | Marks: {self.marks}"
    