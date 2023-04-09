from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from api import serializers
from news.models import News
from houseroom.models import HouseRoom, RoomType, NumberRoom


class NewsListAPIView(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка новостей.
    """
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()

    def get(self, request):
        """Получение списка новостей."""

        return self.list(request)

    def post(self, request, format=None):
        """Добавление новости."""
        return self.create(request)

    def put(self, request, *args, **kwargs):
        """Редактирование новости."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Удаление новости."""
        return self.destroy(request, *args, **kwargs)



class HouseRoomAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка жилья.
    """
    serializer_class = serializers.HouseRoomSerializer

    def get_queryset(self):
        queryset = HouseRoom.objects.all()
        item_name = self.request.query_params.get('city')
        if item_name:
            queryset = queryset.filter(city__contains=item_name.city())
        return queryset

    def get(self, request):
        """Получение списка жилья."""

        return self.list(request)

    def post(self, request, format=None):
        """Добавление информации о жилье."""
        return self.create(request)

