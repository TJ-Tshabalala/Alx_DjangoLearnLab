from django.shortcuts import render
from django.views.generic.list import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
   model = Book
   template_name = 'book_detail.html'
   context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title','author','publication_date']
    template_name = 'book_form.html'

class BookDeleteView(DeleteView):
    model = Book
    fields = ['title','author','publication_date']
    success_url = reverse_lazy('book-list')
# Create your views here.
