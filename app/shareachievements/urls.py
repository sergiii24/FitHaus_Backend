from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shareachievements import views

router = DefaultRouter()
router.register(r'shareachievement', views.ShareAchievementViewSet, basename='shareachievements')

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
