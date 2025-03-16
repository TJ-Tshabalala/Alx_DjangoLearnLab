from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('books/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create', views.BookCreateView.as_view(), name='book-create'),
    path('books/update', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete', views.BookDeleteView.as_view(), name='book-delete'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]