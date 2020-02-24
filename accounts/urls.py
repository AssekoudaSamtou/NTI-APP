from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('profile/', views.view_profile, name="view_profile"),
    path('profile/update_infos_perso', views.update_infos_perso, name="update_infos_perso"),
    path('profile/update_contacts', views.update_contacts, name="update_contacts"),
    path('profile/change_pwd', views.change_pwd, name="change_pwd"),
    path('profile/change_avatar', views.change_avatar, name="change_avatar"),
]
