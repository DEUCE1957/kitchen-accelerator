from django.contrib import admin
from main.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ["views", "likes"]


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["title"]}),
        ("Information", { "fields": ["url", "views"]}),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)