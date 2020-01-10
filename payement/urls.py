from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="payements"),
    path('ajouter/', views.ajouter, name="ajouter_payement"),
    path('modifier/<int:pk>', views.modifier, name="modifier_payement"),
    path('supprimer/<int:pk>', views.supprimer, name="supprimer_payement"),
]
