from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('fetchall/', views.FetchAll, name='fetchall'),
    path('edit/<int:uid>/', views.update, name='update'),
    path('harddelete/<int:uid>/', views.hardDelete, name='hardDelete'),
    path('softdelete/<int:uid>/', views.softDelete, name='softDelete'),
]
