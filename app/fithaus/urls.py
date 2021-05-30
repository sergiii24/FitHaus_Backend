"""fithaus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='users'),
    path('', include('categories.urls'), name='categories'),
    path('', include('exercises.urls'), name='exercises'),
    path('', include('classes.urls'), name='classes'),
    path('', include('objectives.urls'), name='objectives'),
    path('', include('trainings.urls'), name='trainings'),
    path('', include('PredefinedRoutine.urls'), name='predefinedroutines'),
    path('', include('CustomRoutine.urls'), name='customroutines'),
    path('', include('programs.urls'), name='programs'),
    path('', include('colections.urls'), name='collections'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)