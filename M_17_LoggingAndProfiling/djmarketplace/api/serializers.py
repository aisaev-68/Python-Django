from rest_framework import serializers
from app_users.models import Profile
from order.models import Order, OrderItem
from product.models import Product
from shopapp.models import Shop
from payment.models import Billing


class ProfileSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Профиля"""

    class Meta:
        model = Profile
        fields = ('id', 'avatar', "user", 'country', 'postal_code', 'city', 'address', "phone",)


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Заказов"""
    class Meta:
        model = Order
        fields = ('id', "delivery_address", "promocode", "created_at", "user", "paid",)


class OrderItemSerializer(serializers.ModelSerializer):
    """Сериалайзер модели OrderItem"""
    class Meta:
        model = OrderItem
        fields = ('id', "product", "total_price", "quantity",)


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Product"""
    class Meta:
        model = Product
        fields = ("id", "name", "shops", "description", "attributes", "rating", "created_by", "created_at", "price",
                  "discount", "new_price", "image", "products_count", "sold", "archived", "brand",)


class ShopSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Shop"""
    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', )


class BillingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Billing"""
    class Meta:
        model = Billing
        fields = ('id', 'user', 'created_at', 'replenishment_amount', 'balance' )