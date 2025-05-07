from rest_framework import serializers
from .models import News, Category, Subcategory, Service



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Service
        fields = "__all__"

class SubcategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model  = Subcategory
        fields = ("id", "name", "category", "services")

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model  = Category
        fields = ("id", "name", "subcategories")

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
