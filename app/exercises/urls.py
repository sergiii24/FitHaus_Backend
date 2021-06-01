from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exercises import views


router = DefaultRouter()
router.register(r'exercises', views.ExercisesViewSet, basename='exercises')

urlpatterns = [
    path('', include(router.urls))
]