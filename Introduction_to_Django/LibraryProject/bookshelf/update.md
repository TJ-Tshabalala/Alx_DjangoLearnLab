from bookshelf.models import Book

Book.objects.filter(id=1).update(book.title = "Nineteen Eighty-Four")
