from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
]
