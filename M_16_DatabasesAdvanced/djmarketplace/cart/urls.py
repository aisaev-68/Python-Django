from django.urls import path

from cart.views import CartDetail, CartAdd, CartUpdate, CartDelete

app_name = "cart"
urlpatterns = [
    path('all/', CartDetail.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartAdd.as_view(), name='cart_add'),
    path('update/<int:product_id>/', CartUpdate.as_view(), name='cart_update'),
    path('remove/<int:product_id>/', CartDelete.as_view(), name='cart_remove'),
]
