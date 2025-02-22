from django.db import models
from django.db.models import Model
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    
    return self.title
class Library(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ManyToManyField(Book)
    return self.name

class Librarian(models.Model):
    name = models.CharField(max_length = 100)
    library = models.OneToOneField(Library,on_delete = models.CASCADE)

    return self.name
