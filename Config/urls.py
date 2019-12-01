"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from TestModel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TestModel/', include('TestModel.urls')),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('Bike_query/', views.Bike_query),
    path('CyclingR_add/', views.CyclingRecords_add),
    path('CyclingR_query/', views.CyclingRecords_query),
    path('CyclingR_del/', views.CyclingRecords_del),
    path('CyclingR_update/', views.CyclingRecords_update),
    #path('',include('TestModel.urls')),
]
