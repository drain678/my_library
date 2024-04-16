# Generated by Django 5.0.3 on 2024-04-15 12:21

import django.db.models.deletion
import library_app.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_created], verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_modified], verbose_name='modified')),
                ('full_name', models.TextField(verbose_name='full name')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
                'db_table': '"library"."author"',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_created], verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_modified], verbose_name='modified')),
                ('title', models.TextField(verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('type', models.TextField(blank=True, choices=[('book', 'book'), ('magazine', 'magazine')], null=True, verbose_name='type')),
                ('year', models.IntegerField(blank=True, null=True, validators=[library_app.models.check_year], verbose_name='year')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'db_table': '"library"."book"',
                'ordering': ['title', 'type', 'year'],
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_created], verbose_name='created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.author', verbose_name='author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book', verbose_name='book')),
            ],
            options={
                'verbose_name': 'relationship book author',
                'verbose_name_plural': 'relationships book author',
                'db_table': '"library"."book_author"',
                'unique_together': {('book', 'author')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='library_app.BookAuthor', to='library_app.author', verbose_name='authors'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='library_app.BookAuthor', to='library_app.book', verbose_name='books'),
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_created], verbose_name='created')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book', verbose_name='book')),
            ],
            options={
                'verbose_name': 'relationship book genre',
                'verbose_name_plural': 'relationships book genre',
                'db_table': '"library"."book_genre"',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_created], verbose_name='created')),
                ('modified', models.DateTimeField(blank=True, default=library_app.models.get_datetime, null=True, validators=[library_app.models.check_modified], verbose_name='modified')),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('books', models.ManyToManyField(through='library_app.BookGenre', to='library_app.book', verbose_name='books')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': '"library"."genre"',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bookgenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.genre', verbose_name='genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(through='library_app.BookGenre', to='library_app.genre', verbose_name='genres'),
        ),
        migrations.AlterUniqueTogether(
            name='bookgenre',
            unique_together={('book', 'genre')},
        ),
    ]
