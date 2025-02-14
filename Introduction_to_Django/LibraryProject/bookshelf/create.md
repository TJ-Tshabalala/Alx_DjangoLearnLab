from bookshelf.models import Book
Book.objects.all()
book1 = Book.objects.create(1984, 'George Orwell', 1949)

# expected output is 1984, George Orwell, 1949
