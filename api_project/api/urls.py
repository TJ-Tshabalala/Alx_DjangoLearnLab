from django.urls import path
from.views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books',BookViewSet, basename='book_all')
urlpatterns =[
    # Route for the BookList View (ListAPIView)
    path('books/', BookList.as_view(), name='book_list')
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('',include(router.urls)), # This includes all routes to registered with the router
]