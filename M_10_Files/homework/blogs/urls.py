from django.urls import path
from django.views.generic import RedirectView

from .views import ShowBlogs, CreateBlog, BlogDetail, SendMessage


app_name = "blogs"
urlpatterns = [
    path("", ShowBlogs.as_view(), name="show_blogs"),
    path("to_shop/", RedirectView.as_view(url='/shopapp/', permanent=True), name="to_shop"),
    path("to_login/", RedirectView.as_view(url='login', permanent=True), name="to_login"),
    path("detail_blog/<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("user/<int:pk>/", ShowBlogs.as_view(), name="show_blogs"),
    path("create/", CreateBlog.as_view(), name="created_blog"),
    path("send_message/", SendMessage.as_view(), name="send_message"),
]

