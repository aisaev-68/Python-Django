from . import models
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('id', 'first_name', 'last_name', 'year_birth')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'isbn', 'publication_date', 'pages', 'authors')
