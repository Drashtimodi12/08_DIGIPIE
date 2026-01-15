from django.db import models

# Create your models here.

# ------------------------------------------
# Author
# ------------------------------------------
class Author(models.Model):
    Author_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Author_Name
    

# ------------------------------------------
# Publication
# ------------------------------------------
class Publication(models.Model):
    Publication_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Publication_Name
    

# ------------------------------------------
# Book
# ------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} | {self.price} | {self.author} | {self.publication}"
