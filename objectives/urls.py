from django.urls import path, include
from rest_framework.routers import DefaultRouter
from objectives import views


router = DefaultRouter()
router.register(r'objectives', views.ObjectiveViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
