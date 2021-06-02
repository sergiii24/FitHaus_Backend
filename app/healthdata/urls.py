from django.urls import path, include
from healthdata import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'healthdata', views.HealthDataViewSet, basename="healthdata")

urlpatterns = [
    path('', include(router.urls))
]
