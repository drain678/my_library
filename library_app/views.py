from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
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
def create_listview(model_class, plural_name, template):
    class CustomListView(ListView):
        model = model_class
        template_name = template
        paginate_by = 10
        context_object_name = plural_name

        def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            instances = model_class.objects.all()
            paginator = Paginator(instances, 10)
            page = self.request.GET.get('page')
            page_obj = paginator.get_page(page)
            context[f'{plural_name}_list'] = page_obj
            return context
    return CustomListView
BookListView = create_listview(Book, 'books', 'catalog/books.html')
GenreListView = create_listview(Genre, 'genres', 'catalog/genres.html')
AuthorListView = create_listview(Author, 'authors', 'catalog/authors.html')
    
def create_view(model, model_name, template):
    def view(request):
        target = model.objects.get(id=request.GET.get('id', ''))
        return render(
            request,
            template,
            context={model_name: target},
        )
    return view
book_view = create_view(Book, 'book', 'entities/book.html')
author_view = create_view(Author, 'author', 'entities/author.html')
genre_view = create_view(Genre, 'genre', 'entities/genre.html')