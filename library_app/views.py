from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Book, Author, Genre, Client
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer
from .forms import RegistrationForm, TestForm


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
        id_ = request.GET.get('id', None)
        target = model.objects.get(id=id_) if id_ else None
        return render(
            request,
            template,
            context={model_name: target},
        )
    return view
book_view = create_view(Book, 'book', 'entities/book.html')
author_view = create_view(Author, 'author', 'entities/author.html')
genre_view = create_view(Genre, 'genre', 'entities/genre.html')

def create_viewset(model_class, serializer):
    class CustomViewSet(ModelViewSet):
        queryset = model_class.objects.all()
        serializer_class = serializer

    return CustomViewSet

BookViewSet = create_viewset(Book, BookSerializer)
AuthorViewSet = create_viewset(Author, AuthorSerializer)
GenreViewSet = create_viewset(Genre, GenreSerializer)

def test_form(request):
    context = {'form': TestForm()}
    for key in ('text', 'choice', 'number'):
        context[key] = request.GET.get(key, None)
        return render(request, 'pages/test_form.html', context)
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)
        else:
            errors = form.errors
    else:
        form = RegistrationForm()
    
    return render(request, 'regisration/register.html', {
        'form': form,
        'errors': errors,
    })
