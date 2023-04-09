from django.contrib import admin

from houseroom.models import HouseRoom, NumberRoom, RoomType


@admin.register(HouseRoom)
class HouseRoomAdmin(admin.ModelAdmin):

    list_display = "pk", "city", "address", "developer", "floors"
    list_display_links = "city", "address"
    search_fields = "city", "address", "developer"


@admin.register(NumberRoom)
class NumberRoomAdmin(admin.ModelAdmin):

    list_display = "pk", "house", "room_count", "storey", "total_area", "kitchen_area", "living_space", "price"

    list_display_links = "pk", "price"
    search_fields = "storey", "living_space", "price"


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = "pk", "room", "type_name"

    list_display_links = "pk", "type_name"
    search_fields = "type_name",