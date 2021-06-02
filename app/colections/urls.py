from colections import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'colections', views.colectionsViewSet, basename='colections')

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
