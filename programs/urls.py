from django.urls import path, include
from rest_framework.routers import DefaultRouter
from programs import views


router = DefaultRouter()
router.register(r'programs', views.RoutineViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
