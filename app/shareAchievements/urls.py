from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shareAchievements import views


router = DefaultRouter()
router.register(r'shareachievement', views.ShareAchievementViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
