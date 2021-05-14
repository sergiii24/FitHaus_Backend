from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CustomRoutine import views


router = DefaultRouter()
router.register(r'customroutines', views.CustomRoutinesViewSet)

urlpatterns = [
    path('', include(router.urls))
]