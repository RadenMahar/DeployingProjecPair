from django.contrib import admin
from django.urls import path
# from .views import *
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('detail/<int:id_lowongan>', views.detail, name="detail"),
    path('Detail/', views.Detail, name="Detail"),
]
