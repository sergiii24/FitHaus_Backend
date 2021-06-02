from customroutines import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customroutines', views.CustomRoutinesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
