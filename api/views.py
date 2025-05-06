from rest_framework import viewsets
from .models import CatalogItem, News
from .serializers import CatalogItemSerializer, NewsSerializer

class CatalogItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogItem.objects.all().order_by('category', 'subcategory', 'name')
    serializer_class = CatalogItemSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
