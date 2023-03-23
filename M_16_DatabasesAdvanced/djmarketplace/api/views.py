from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from api import serializers
from app_users.models import Profile
from product import models


class ProfileListAPIView(ListModelMixin, GenericAPIView):
    """
    Представление для получения списка профилей
    """
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        """Получение списка профилей."""

        return self.list(request)


class ProductListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка продуктов и добавления нового продукта
    """
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name__contains=item_name.title())
        return queryset

    def get(self, request):
        """Получение списка продуктов."""

        return self.list(request)

    def post(self, request, format=None):
        """Добавление информации о продукте."""
        return self.create(request)


class ProductDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    Представление для получения детальной информации о продукте, редактировании и удалении.
    """
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def get(self, request, *args, **kwargs):
        """Получение детальной информации о продукте."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Редактирование информации о продукте."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Удаление информации о продукте."""
        return self.destroy(request, *args, **kwargs)

