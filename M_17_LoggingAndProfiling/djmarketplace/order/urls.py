from django.urls import path, include

from order.views import OrderList, OrderCreate, OrderListByUser, OrderDetail, UpdateOrder, OrderDelete, OrdersExport

name = "order"
urlpatterns = [
    path("", OrderList.as_view(), name="orders_list"),
    path("export/", OrdersExport.as_view(), name="orders_export"),
    path("create/", OrderCreate.as_view(), name="create_order"),
    path("user/<int:pk>/", OrderListByUser.as_view(), name="orders_user"),
    path("detail/<int:pk>/", OrderDetail.as_view(), name="order_detail"),
    path("update/<int:pk>/", UpdateOrder.as_view(), name="update_order"),
    path("delete/<int:pk>/", OrderDelete.as_view(), name="order_delete"),
    ]