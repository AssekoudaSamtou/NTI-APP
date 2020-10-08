from django.urls import path

from . import views
from investissement import views as investissement_views

urlpatterns = [
    path('', views.index, name="investisseurs"),
    path('ajouter/', views.ajouter, name="ajouter_investisseur"),
    path('<int:pk>/ajouter_investissement/', investissement_views.ajouter, name="ajouter_investissement_investisseur"),
    path('modifier/<int:pk>/', views.modifier, name="modifier_investisseur"),
    path('supprimer/<int:pk>/', views.supprimer, name="supprimer_investisseur"),

    path('espace/', views.espace, name="espace_investisseur"),
    path('espace/investissements', views.liste_investissements, name="investissements_investisseur"),
    path('espace/payements', views.liste_payements, name="payements_investisseur"),
    path('espace/filleuls', views.liste_filleuls, name="filleuls"),
]
