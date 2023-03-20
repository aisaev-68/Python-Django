from django.urls import path
from . import views

app_name = "bookapi"
urlpatterns = [
    path('authors/', views.AuthorListAPIView.as_view(), name='api_authors'),
    path('books/', views.BookListAPIView.as_view(), name='api_books'),
]