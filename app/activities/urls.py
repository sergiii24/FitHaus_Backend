from django.urls import path, include
from rest_framework.routers import DefaultRouter
from activities import views


router = DefaultRouter()
router.register(r'activities', views.ActivitiesViewSet)

urlpatterns = [
    path('', include(router.urls))
]