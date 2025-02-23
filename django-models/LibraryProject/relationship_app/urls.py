# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/',LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register_view, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/',views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
     path('books/add/', views.add_book, name='add_book'),
    path('books/nge/<int:pk>/', views.change_book, name='change_book'),
    path('books/edit/<int:pk>/', views.change_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
        ]
