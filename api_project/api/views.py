from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import HttpReponse
from django.urls import path


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# Create your views here.
