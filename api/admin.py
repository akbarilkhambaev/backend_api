from django.contrib import admin
from .models import CatalogItem, News

@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'subcategory', 'name')
    list_filter = ('category', 'subcategory')
    search_fields = ('name', 'category', 'subcategory')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
