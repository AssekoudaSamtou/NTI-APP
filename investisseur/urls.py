from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="investisseurs"),
    path('ajouter/', views.ajouter, name="ajouter_investisseur"),
    path('modifier/<int:pk>/', views.modifier, name="modifier_investisseur"),
    path('supprimer/<int:pk>/', views.supprimer, name="supprimer_investisseur"),

    path('espace/', views.espace, name="espace_investisseur"),
    path('espace/investissements', views.liste_investissements, name="investissements_investisseur"),
    path('espace/filleuls', views.liste_filleuls, name="filleuls"),
]
