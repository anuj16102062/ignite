from rest_framework import serializers
from .models import Author, Book, BookLanguage

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_year', 'death_year']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = [
            'title', 'author', 'language_id', 'subjects_id',
            'bookshelves', 'download_links', 'download_count'
        ]

class BookLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLanguage
        fields = '__all__'
