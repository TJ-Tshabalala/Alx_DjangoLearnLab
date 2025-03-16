from django.shortcuts import render
from django.views.generic.list import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
   model = Book
   template_name = 'book_detail.html'
   context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title','author','publication_date']
    template_name = 'book_form.html'

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    fields = ['title','author','publication_date']
    success_url = reverse_lazy('book-list')
# Create your views here.
# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read for all, write for authenticated

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read for all, write for authenticated