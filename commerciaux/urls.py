from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="commerciaux"),
    path('ajouter/', views.ajouter, name="ajouter_commercial"),
    path('modifier/<int:pk>', views.modifier, name="modifier_commercial"),
    path('supprimer/<int:pk>', views.supprimer, name="supprimer_commercial"),
]
