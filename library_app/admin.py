from django.contrib import admin

from .models import Author, Genre, Book, BookAuthor, BookGenre

class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1

class BookGenreInline(admin.TabularInline):
    model = BookGenre
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = (BookAuthorInline,)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = (BookGenreInline, BookAuthorInline)

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    model = BookAuthor

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    model = BookGenre