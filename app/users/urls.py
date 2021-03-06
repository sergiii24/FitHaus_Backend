from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register(r'users', views.UserList, basename="users")

urlpatterns = [
    path('users/login', views.login),
    path('users/stats', views.stats),
    path('ranking', views.UserRankingViewSet.as_view({'get': 'list'})),
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
