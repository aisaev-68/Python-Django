from django.urls import path
from django.contrib.auth import views

from product.views import ShowProductsPage, TopSellingReport, ProductList, CreateProduct, DetailProduct, UpdateProduct, ArchivedProduct

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
    path("top_selling_report/", TopSellingReport.as_view(), name="top_selling_report"),
]