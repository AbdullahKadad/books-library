from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

class TestHomePage(SimpleTestCase):
    def test_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

class TestBooksPage(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.user,
            description='A test book description.',
            rating=4.5,
            publish_date='2024-07-16'
        )

    def test_status(self):
        url = reverse('books')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('books')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'books.html')

class TestBookDetailsPage(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.user,
            description='A test book description.',
            rating=4.5,
            publish_date='2024-07-16'
        )

    def test_status(self):
        url = reverse('bookdetails', kwargs={'pk': self.book.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('bookdetails', kwargs={'pk': self.book.pk})
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'bookDetails.html')
