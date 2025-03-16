# api/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', author=self.author, publication_date='2023-01-01')
        self.client.login(username=self.username, password=self.password) #Using self.client.login

    def test_book_list_create(self):
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        data = {'title': 'New Book', 'author_id': self.author.id, 'publication_date': '2024-01-01'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_retrieve_update_destroy(self):
        url = reverse('book-retrieve-update-destroy', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

        data = {'title': 'Updated Book', 'author_id': self.author.id, 'publication_date': '2024-01-01'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, 'Updated Book')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_filtering(self):
        url = reverse('book-list-create') + '?title=Test%20Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_book_search(self):
        url = reverse('book-list-create') + '?search=Test%20Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], 'Test Author')

    def test_book_ordering(self):
        Book.objects.create(title='Another Book', author=self.author, publication_date='2022-01-01')
        url = reverse('book-list-create') + '?ordering=publication_date'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

    def test_unauthenticated_read_only(self):
        self.client.logout() #logout the client.
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'title': 'New Book', 'author_id': self.author.id, 'publication_date': '2024-01-01'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)