from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, BookLanguage
from .serializers import AuthorSerializer, BookSerializer, BookLanguageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Book


class BookListView(APIView):
    def get(self, request):
        # Filters from query params
        book_ids = request.GET.getlist('book_id')
        languages = request.GET.get('language', '').split(',')
        mime_types = request.GET.get('mime_type', '').split(',')
        topics = request.GET.get('topic', '').split(',')
        authors = request.GET.get('author', '').split(',')
        titles = request.GET.get('title', '').split(',')

        # Base queryset
        queryset = Book.objects.all()

        # Apply filters
        if book_ids:
            queryset = queryset.filter(gutenberg_id__in=book_ids)
        if languages:
            queryset = queryset.filter(language_id__in=languages)
        if mime_types:
            queryset = queryset.filter(mime_type__in=mime_types)
        if topics:
            topic_query = Q()
            for topic in topics:
                topic_query |= Q(subjects_id__icontains=topic) | Q(bookshelves__icontains=topic)
            queryset = queryset.filter(topic_query)
        if authors:
            author_query = Q()
            for author in authors:
                author_query |= Q(author__name__icontains=author)
            queryset = queryset.filter(author_query)
        if titles:
            title_query = Q()
            for title in titles:
                title_query |= Q(title__icontains=title)
            queryset = queryset.filter(title_query)

        # Order by popularity (download_count)
        queryset = queryset.order_by('-download_count')

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 25
        result_page = paginator.paginate_queryset(queryset, request)

        # Serialize and return response
        serializer = BookSerializer(result_page, many=True)
        print(serializer.data,'============62')
        return paginator.get_paginated_response(serializer.data)

class AuthorCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookLanguageCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookLanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
