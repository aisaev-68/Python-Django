from django.contrib import admin

from houseroom.models import HouseRoom, NumberRoom, RoomType, Room


@admin.register(HouseRoom)
class HouseRoomAdmin(admin.ModelAdmin):

    list_display = "pk", "city", "address", "developer", "floors", "created_at"
    list_display_links = "city", "address"
    search_fields = "city", "address", "developer"


@admin.register(NumberRoom)
class NumberRoomAdmin(admin.ModelAdmin):
    list_display = "pk", "room_count"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = "pk", "house", "storey", \
        "total_area", "price", "room_number", "room_type"

    list_display_links = "pk", "price"
    search_fields = "storey", "price"


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = "pk", "type_name"

    list_display_links = "pk", "type_name"
    search_fields = "type_name",