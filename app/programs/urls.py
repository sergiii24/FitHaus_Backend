from django.urls import path, include
from programs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', views.ProgramsViewSet, basename='programs')

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
