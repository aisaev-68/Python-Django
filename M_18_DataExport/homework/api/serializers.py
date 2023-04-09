from rest_framework import serializers
from news.models import News
from houseroom.models import HouseRoom, RoomType, NumberRoom



class HouseRoomSerializer(serializers.ModelSerializer):
    """Сериалайзер модели HouseRoom"""

    class Meta:
        model = HouseRoom
        fields = ("id", "city", "address", "developer", "floors",)


class RoomTypeSerializer(serializers.ModelSerializer):
    """Сериалайзер модели RoomType"""
    class Meta:
        model = RoomType
        fields = ('id', "room", "room_type",)


class NumberRoomSerializer(serializers.ModelSerializer):
    """Сериалайзер модели NumberRoom"""
    class Meta:
        model = NumberRoom
        fields = ('id', "house", "room_count", "storey", "total_area", "kitchen_area", "living_space", "price",)


class NewsSerializer(serializers.ModelSerializer):
    """Сериалайзер модели News"""
    class Meta:
        model = News
        fields = ("id", "title", "description", "created_at", "published",)

