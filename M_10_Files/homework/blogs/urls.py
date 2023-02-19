from django.urls import path

from .views import ShowBlogs, CreateBlog

app_name = "blogs"
urlpatterns = [
    path("", ShowBlogs.as_view(), name="show_blogs"),
    path("user/<int:pk>/", ShowBlogs.as_view(), name="show_blogs"),
    path("create/", CreateBlog.as_view(), name="created_blog"),
]

