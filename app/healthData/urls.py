from django.urls import path, include
from rest_framework.routers import DefaultRouter
from healthData import views


router = DefaultRouter()
router.register(r'healthdata', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
