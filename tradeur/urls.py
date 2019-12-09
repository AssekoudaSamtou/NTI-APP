from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="tradeurs"),
    path('ajouter/', views.ajouter, name="ajouter_tradeur"),
    path('profile/<int:pk>/', views.profile, name="profile_tradeur"),
]
