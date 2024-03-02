from django.contrib import admin
from django.urls import path
from app.views import *
from . import views

urlpatterns = [  
    path('', views.home, name='home'),
    path('maintainance/', views.home, name='maintainance'),
    path('description/<int:id>', views.description, name='description'),
    path('enable/<int:id>', views.enable_state, name='enable_state'),
    path('disable/<int:id>', views.disable_state, name='disable_state'),
    path('chart/', views.chart_disp, name='chart_disp'),
    
]
