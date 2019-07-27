from django.contrib import admin
from main.models import User, Kitchen, Members, Fridge, Shelf, Cell, Oven, Stove


class UserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "password", "email", "profile_picture"]


class KitchenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["name","location"]}),
        ("Information", { "fields": ["fridges", "ovens", "stoves"]}),
    ]

class MembersAdmin(admin.ModelAdmin):
    fields = ["user_id", "kitchen_id"]

class FridgeAdmin(admin.ModelAdmin):
    fields = ["kitchen", "full"]

class ShelfAdmin(admin.ModelAdmin):
    fields = ["fridge", "full"]

class CellAdmin(admin.ModelAdmin):
    fields = ["shelf", "full"]

class OvenAdmin(admin.ModelAdmin):
    fields = ["kitchen", "free"]

class StoveAdmin(admin.ModelAdmin):
    fields = ["kitchen", "type", "free"]

admin.site.register(User, UserAdmin)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Oven, OvenAdmin)
admin.site.register(Stove, StoveAdmin)