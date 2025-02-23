# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
        ]
