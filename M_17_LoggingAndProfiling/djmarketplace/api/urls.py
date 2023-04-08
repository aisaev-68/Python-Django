from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('profiles/', views.ProfileListAPIView.as_view(), name='api_profiles'),
    path('products/list/', views.ProductListAPIView.as_view(), name='api_product_list'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='api_book_detail'),
]