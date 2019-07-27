from django.contrib import admin
from main.models import User, Kitchen


class UserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "password", "email", "profile_picture"]


class KitchenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["name","location"]}),
        ("Information", { "fields": ["fridges", "ovens", "stoves"]}),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Kitchen, KitchenAdmin)