from django.contrib import admin
from main.models import UserProfile, Kitchen, Members, Fridge, Shelf, Cell, Oven, Stove


class KitchenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["name","location","slug"]}),
        ("Information", { "fields": ["fridges", "ovens", "stoves"]}),
    ]

    list_display = ("name", "location", "fridges", "ovens", "stoves")


class MembersAdmin(admin.ModelAdmin):
    fields = ["user_id", "kitchen_id"]

    list_display = ("user_id", "kitchen_id")


class FridgeAdmin(admin.ModelAdmin):
    fields = ["id","kitchen", "full"]

    list_display = ("kitchen", "full")


class ShelfAdmin(admin.ModelAdmin):
    fields = ["id","fridge", "full"]

    list_display = ("fridge", "full")


class CellAdmin(admin.ModelAdmin):
    fields = ["id","shelf", "full"]

    list_display = ("shelf", "full")


class OvenAdmin(admin.ModelAdmin):
    fields = ["kitchen", "free"]

    list_display = ("kitchen", "free")


class StoveAdmin(admin.ModelAdmin):
    fields = ["kitchen", "type", "free"]

    list_display = ("kitchen", "type", "free")


admin.site.register(UserProfile)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Oven, OvenAdmin)
admin.site.register(Stove, StoveAdmin)