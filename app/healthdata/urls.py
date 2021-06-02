from django.urls import path, include
from rest_framework.routers import DefaultRouter
from healthdata import views


router = DefaultRouter()
router.register(r'healthdata', views.HealthDataViewSet, basename="healthdata")

urlpatterns = [
    path('', include(router.urls))
]