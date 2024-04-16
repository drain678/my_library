from  django.test import TestCase
from django.test.client import Client
from django.urls import reverse

OK = 200


def create_view_test(url, page_name, template):
    class ViewTest(TestCase):
        def setUp(self):
            self.client = Client()

        def test_view_exists_by_url(self):
            response = self.client.get(url)
            self.assertEqual(response.status_code, OK)

        def test_view_exists_by_name(self):
            responce = self.client.get(reverse(page_name))
            self.assertEqual(responce.status_code, OK)

        def test_view_uses_template(self):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)
    return ViewTest

BooksViewTest = create_view_test('/books/', 'books', 'catalog/books.html')
GenresViewTest = create_view_test('/genres/', 'genres', 'catalog/genres.html')
AuthorsViewTest = create_view_test('/authors/', 'authors', 'catalog/authors.html')

BookViewTest = create_view_test('/book/', 'book', 'entities/book.html')
GenreViewTest = create_view_test('/genre/', 'genre', 'entities/genre.html')
AuthorViewTest = create_view_test('/author/', 'author', 'entities/author.html')
