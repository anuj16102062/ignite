from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'books_author'
        managed = True

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    
    gutenberg_id = models.CharField(max_length=255)
    language_id = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=50,default="")
    subjects_id = models.TextField()
    bookshelves = models.TextField()
    download_links = models.JSONField()
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class BookLanguage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='languages')
    language_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_languages'
        managed = True

    def __str__(self):
        return f"Book: {self.book.title}, Language ID: {self.language_id}"

