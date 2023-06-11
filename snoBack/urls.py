"""snoBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.urls import include, re_path
from dataKeeper.views import *
from snoBack.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #News url
    path('news/', NewsData.as_view()),
    path('news/<int:pk>/', NewsData.as_view()),
    
    #Galery url
    path('gal/', GaleryData.as_view()),
    path('gal/<int:pk>/', GaleryData.as_view()),
    
    #Application url
    path("app/", ApplicationData.as_view()),
    path('app/<int:pk>/', ApplicationData.as_view()),
    
    #Calendar url
    path("cal/", CalendarData.as_view()),
    path("cal/<int:pk>/", CalendarData.as_view()),
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
