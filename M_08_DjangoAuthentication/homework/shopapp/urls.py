from django.urls import path

from .views import (
    ShopPage,
    UserLogIn,
    UserLogOut,
    ProductList,
    OrderList,
    CreateProduct,
    OrderCreate,
    UpdateProduct,
    UpdateOrder,
    DetailProduct,
    ArchivedProduct,
    OrderDetail,
    OrderDelete,
)

app_name = "shopapp"

urlpatterns = [
    path("", ShopPage.as_view(), name="shop_page"),
    path("login/", UserLogIn.as_view(), name="login"),
    path("logout/", UserLogOut.as_view(), name="logout"),
    path("products/", ProductList.as_view(), name="products_list"),
    path("products/create/", CreateProduct.as_view(), name="create_product"),
    path("products/<int:pk>/detail/", DetailProduct.as_view(), name="product_detail"),
    path("products/<int:pk>/update/", UpdateProduct.as_view(), name="update_product"),
    path("products/<int:pk>/archived/", ArchivedProduct.as_view(), name="product_archived"),
    path("orders/", OrderList.as_view(), name="orders_list"),
    path("orders/create/", OrderCreate.as_view(), name="create_order"),
    path("orders/<int:pk>/detail/", OrderDetail.as_view(), name="order_detail"),
    path("orders/<int:pk>/update/", UpdateOrder.as_view(), name="update_order"),
    path("orders/<int:pk>/delete/", OrderDelete.as_view(), name="order_delete"),
]