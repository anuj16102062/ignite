# Generated by Django 3.2.12 on 2024-11-23 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('death_year', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_author',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('gutenberg_id', models.CharField(max_length=255)),
                ('language_id', models.CharField(max_length=50)),
                ('mime_type', models.CharField(default='', max_length=50)),
                ('subjects_id', models.TextField()),
                ('bookshelves', models.TextField()),
                ('download_links', models.JSONField()),
                ('download_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='gutenberg_books.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='gutenberg_books.book')),
            ],
            options={
                'db_table': 'books_book_languages',
                'managed': True,
            },
        ),
    ]
