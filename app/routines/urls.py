from django.urls import path, include
from rest_framework.routers import DefaultRouter
from routines import views

router = DefaultRouter()
router.register(r'routines', views.RoutineViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
