from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, CategoryViewSet, SubcategoryViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r"categories",   CategoryViewSet,   basename="categories")
router.register(r"subcategories",SubcategoryViewSet,basename="subcategories")
router.register(r"services",     ServiceViewSet,    basename="services")
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
