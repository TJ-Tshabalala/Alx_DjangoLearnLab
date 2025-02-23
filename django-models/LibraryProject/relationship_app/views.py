from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

def list_book(request):

    books = Book.objects.all()
    book_list = ""

    for book in books:
        author = ", ".joint([author.name for author in book.authors.all()])
        book_list += f"{book.title} - {authors}\n"

    return HttpResponse(book_list, content_type="tet/plain")
