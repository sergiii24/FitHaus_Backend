from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exercises import views


router = DefaultRouter()
router.register(r'exercises', views.ExercisesViewSet)

urlpatterns = [
    path('', include(router.urls))
]