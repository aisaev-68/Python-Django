from django.urls import path
from django.contrib.auth import views

from product.views import ShowProductsPage, ProductList, CreateProduct, DetailProduct, UpdateProduct, ArchivedProduct

# from .views import ProfileView, AboutMe
#
name = 'product'
urlpatterns = [
    path("<int:pk>/", ShowProductsPage.as_view(), name="products_by_shop"),
    path("all/", ProductList.as_view(), name="products_list"),
    path("create/", CreateProduct.as_view(), name="create_product"),
    path("detail/<int:pk>/", DetailProduct.as_view(), name="product_detail"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path("archived/<int:pk>/", ArchivedProduct.as_view(), name="product_archived"),
    # path("update/", ProfileView.as_view(), name="profile"),
    path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("about_me/<int:pk>/", AboutMe.as_view(), name="about-me"),
]