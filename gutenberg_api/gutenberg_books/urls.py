from django.urls import path
from . import views

urlpatterns = [
    path('author', views.AuthorCreateView.as_view(), name='author-create'),
    path('book/', views.BookCreateView.as_view(), name='book-create'),
    path('book-language/', views.BookLanguageCreateView.as_view(), name='book-language-create'),
    path('books/', views.BookListView.as_view(), name='book-list'),
]
