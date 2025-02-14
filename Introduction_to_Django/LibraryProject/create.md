from bookshelf.models import Book
Book.objects.all()
create_book = Book(1,"1984", "George Orwell", 1949)

# expected output is 1984, George Orwell, 1949
