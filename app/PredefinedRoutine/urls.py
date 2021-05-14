from django.urls import path, include
from rest_framework.routers import DefaultRouter
from PredefinedRoutine import views


router = DefaultRouter()
router.register(r'predefinedroutines', views.PredefinedRoutineViewSet)

urlpatterns = [
    path('', include(router.urls))
]