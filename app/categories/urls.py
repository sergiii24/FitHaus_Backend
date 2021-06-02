from categories import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
