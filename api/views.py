from rest_framework import viewsets
from .models import News, Category, Subcategory, Service
from .serializers import CategorySerializer, SubcategorySerializer, ServiceSerializer
from .serializers import  NewsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset         = Subcategory.objects.select_related("category").all().order_by("name")
    serializer_class = SubcategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset         = Service.objects.select_related("subcategory").all().order_by("name")
    serializer_class = ServiceSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
