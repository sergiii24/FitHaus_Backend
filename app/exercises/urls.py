from django.urls import path, include
from exercises import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'exercises', views.ExercisesViewSet, basename='exercises')

urlpatterns = [
    path('', include(router.urls))
]
