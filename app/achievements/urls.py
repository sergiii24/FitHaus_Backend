from achievements import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'achievements', views.AchievementsViewSet, basename='achievements')

urlpatterns = [
    path('', include(router.urls))
]
