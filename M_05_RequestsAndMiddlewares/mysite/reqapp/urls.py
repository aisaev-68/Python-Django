from django.urls import path
from . import views

app_name = 'reqpapp'
urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
]
