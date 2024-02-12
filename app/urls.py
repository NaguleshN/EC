from django.contrib import admin
from django.urls import path
from app.views import *
from . import views

urlpatterns = [  
    path('', views.home, name='home'),
    path('maintainance/', views.home, name='maintainance'),
    path('description/<int:id>', views.description, name='description'),
]
