from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="exercices"),
    path('ajouter/', views.ajouter, name="ajouter_exercice"),
    path('modifier/<int:pk>/', views.modifier, name="modifier_exercice"),
    path('supprimer/<int:pk>/', views.supprimer, name="supprimer_exercice"),
]
