from django.urls import path, include
from rest_framework.routers import DefaultRouter
from colections import views


router = DefaultRouter()
router.register(r'collections', views.CollectionsViewSet, basename='collections')

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
