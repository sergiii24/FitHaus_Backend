from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('users/login/', views.login),
    path('', include(router.urls))
]
# The API URLs are now determined automatically by the router.
