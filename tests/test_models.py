from django.test import TestCase
from library_app.models import Book, Author, Genre

def create_model_test(model_class, creation_attrs):
    class ModelTest(TestCase):
        def test_successful_creation(self):
            model_class.objects.create(**creation_attrs)
    return ModelTest
    
book_attrs = {'title': 'ABC', 'type': 'DEF', 'volume': 123}
genre_attrs = {'name': 'ABC'}
author_attrs = {'full_name': 'Muhxeem Nudga'}

BookModelTest = create_model_test(Book, book_attrs)
AuthorModelTest = create_model_test(Author, author_attrs)
GenreModelTest = create_model_test(Genre, genre_attrs)
