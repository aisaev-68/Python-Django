from django.urls import path

from .views import shop, ProductList, OrderList, CreateProduct, OrderCreate, UpdateProduct, UpdateOrder, DetailProduct, DeleteProduct

app_name = "shopapp"

urlpatterns = [
    path("", shop, name="shop"),
    path("products/", ProductList.as_view(), name="products_list"),
    path("products/create/", CreateProduct.as_view(), name="create_product"),
    path("products/<int:pk>/detail/", DetailProduct.as_view(), name="product_detail"),
    path("products/<int:pk>/update/", UpdateProduct.as_view(), name="update_product"),
    path("products/<int:pk>/archived/", DeleteProduct.as_view(), name="product_archived"),
    path("orders/", OrderList.as_view(), name="orders_list"),
    path("orders/create/", OrderCreate.as_view(), name="create_order"),
    path("orders/<int:pk>/update/", UpdateOrder.as_view(), name="update_order"),
]
