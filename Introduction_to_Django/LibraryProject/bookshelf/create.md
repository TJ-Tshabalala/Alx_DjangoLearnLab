from bookshelf.models import Book
Book.objects.all()
book1 = Book.objects.create("title","author")

# expected output is 1984, George Orwell, 1949
