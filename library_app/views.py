from django.shortcuts import render
from .models import Book, Author, Genre


def main(request):
    return render(
        request,
        'index.html',
        context={
            'books': Book.objects.count(),
            'authors': Author.objects.count(),
            'genres': Genre.objects.count(),
        }
    )