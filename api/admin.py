from django.contrib import admin
from .models import News, Category, Subcategory, Service

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter  = ("category",)
    search_fields = ("name",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subcategory")
    list_filter  = ("subcategory__category", "subcategory")
    search_fields = ("name",)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

