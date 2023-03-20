from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from . import serializers
from . import models


class AuthorListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        queryset = models.Author.objects.all()
        item_name = self.request.query_params.get('first_name')
        if item_name:
            queryset = queryset.filter(first_name__contains=item_name.title())
        return queryset

    def get(self, request):
        print(11111, request)
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        queryset = models.Book.objects.all()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('authors', 0)
        pages = int(self.request.query_params.get('pages', 0))

        if author and title:
            queryset = queryset.filter(title__contains=title.capitalize()).filter(authors=author)
        elif 100 <= pages < 700:
            queryset = queryset.filter(pages__gte=100).filter(pages__lt=700)
        elif pages == 700:
            queryset = queryset.filter(pages__exact=700)
        elif pages > 700:
            queryset = queryset.filter(pages__gt=700)

        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
