from django.db import models
from uuid import uuid4
from datetime import datetime, timezone, date
from django.core.exceptions import ValidationError
from typing import Callable
from django.utils.translation import gettext_lazy as _

def get_datetime() -> datetime:
    return datetime.now(timezone.utc)

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


def check_modified(dt: datetime) -> None:
    if dt > get_datetime():
        raise ValidationError(
            _('Date and time is bigger than current!'),
            params={'modified': dt}
        )

def check_created(dt: datetime) -> None:
    if dt > get_datetime():
        raise ValidationError(
            _('Date and time is bigger than current!'),
            params={'created': dt}
        )


class CreatedMixin(models.Model):
    created = models.DateTimeField(
        _('created'), null=True, blank=True,
        default=get_datetime, validators=[check_created],
    )

    class Meta:
        abstract = True

class ModifiedMixin(models.Model):
    modified = models.DateTimeField(
        _('modified'), null=True, blank=True,
        default=get_datetime, validators=[check_modified],
    )

    class Meta:
        abstract = True

class Author(UUIDMixin, CreatedMixin, ModifiedMixin):
    full_name = models.TextField(_('full name'), null=False, blank=False)

    books = models.ManyToManyField('Book', verbose_name=_('books'), through='BookAuthor')

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        db_table = '"library"."author"'
        ordering = ['full_name']
        verbose_name = _('author')
        verbose_name_plural = _('authors')

class Genre(UUIDMixin, CreatedMixin, ModifiedMixin):
    name = models.TextField(_('name'), null=False, blank=False)
    description = models.TextField(_('description'), null=True, blank=True)

    books = models.ManyToManyField('Book', verbose_name=_('books'), through='BookGenre')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = '"library"."genre"'
        ordering = ['name']
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

def check_year(year: int) -> None:
    if year > date.today().year:
        raise ValidationError(
            _('Year is bigger than current year!'),
            params={'year': year},
        )

book_types = (
    ('book', _('book')),
    ('magazine', _('magazine')),
)

class Book(UUIDMixin, CreatedMixin, ModifiedMixin):
    title = models.TextField(_('title'), null=False, blank=False)
    description = models.TextField(_('description'), null=True, blank=True)
    volume = models.PositiveIntegerField(_('volume'), null=False, blank=False)
    type = models.TextField(_('type'), null=True, blank=True, choices=book_types)
    year = models.IntegerField(_('year'), null=True, blank=True, validators=[check_year])

    authors = models.ManyToManyField(Author, verbose_name=_('authors'), through='BookAuthor')
    genres = models.ManyToManyField(Genre, verbose_name=_('genres'), through='BookGenre')

    def __str__(self) -> str:
        return f'"{self.title}", {self.type}, {self.volume} pages'

    class Meta:
        db_table = '"library"."book"'
        ordering = ['title', 'type', 'year']
        verbose_name = _('book')
        verbose_name_plural = _('books')

class BookGenre(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, verbose_name=_('book'), on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name=_('genre'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.book} - {self.genre}'

    class Meta:
        db_table = '"library"."book_genre"'
        unique_together = (
            ('book', 'genre'),
        )
        verbose_name = _('relationship book genre')
        verbose_name_plural = _('relationships book genre')

class BookAuthor(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, verbose_name=_('book'), on_delete=models.CASCADE)
    author = models.ForeignKey(Author, verbose_name=_('author'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.book} - {self.author}'

    class Meta:
        db_table = '"library"."book_author"'
        unique_together = (
            ('book', 'author'),
        )
        verbose_name = _('relationship book author')
        verbose_name_plural = _('relationships book author')