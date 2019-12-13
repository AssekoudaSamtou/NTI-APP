from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="investisseurs"),
    path('ajouter/', views.ajouter, name="ajouter_investisseur"),
    path('modifier/<int:pk>/', views.modifier, name="modifier_investisseur"),
    path('supprimer/<int:pk>/', views.supprimer, name="supprimer_investisseur"),
]
