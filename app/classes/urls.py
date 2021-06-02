from classes import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', views.ClassViewSet, basename='exercises')

urlpatterns = [
    path('', include(router.urls))
]
