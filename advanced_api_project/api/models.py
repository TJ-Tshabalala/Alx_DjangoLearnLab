from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 255)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateField('publised')
    author = models.OnetoManyField(Author, on_delete = models.CASCADE)