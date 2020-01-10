from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="exercices"),
    path('ajouter/', views.ajouter, name="ajouter_exercice"),
    path('profile/<int:pk>/', views.modifier, name="profile_exercice"),
    path('supprimer/<int:pk>/', views.supprimer, name="supprimer_exercice"),
]
