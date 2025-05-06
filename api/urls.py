from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CatalogItemViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'catalog', CatalogItemViewSet, basename='catalog')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
