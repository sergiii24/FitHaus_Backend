from django.urls import path, include
from rest_framework.routers import DefaultRouter
from trainings import views


router = DefaultRouter()
router.register(r'trainings', views.TrainingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
