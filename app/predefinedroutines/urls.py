from django.urls import path, include
from predefinedroutines import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'predefinedroutines', views.PredefinedRoutineViewSet)

urlpatterns = [
    path('', include(router.urls))
]
