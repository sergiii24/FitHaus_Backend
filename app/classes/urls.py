from django.urls import path, include
from rest_framework.routers import DefaultRouter
from classes import views


router = DefaultRouter()
router.register(r'classes', views.ClassViewSet)

urlpatterns = [
    path('', include(router.urls))
]