from django.urls import path, include
from predefinedroutine import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'predefinedroutines', views.PredefinedRoutineViewSet)

urlpatterns = [
    path('', include(router.urls))
]