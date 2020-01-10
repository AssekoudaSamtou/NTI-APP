"""dashmed_heroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from dashmed_heroku import settings
from dashmed_heroku._views import home

admin.autodiscover()

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
	path('brokers/', include('broker.urls')),
	path('comptes/', include('compte.urls')),
	path('tradeurs/', include('tradeur.urls')),
	path('payements/', include('payement.urls')),
	path('exercices/', include('exercice.urls')),
	path('operations/', include('operation.urls')),
	path('commerciaux/', include('commerciaux.urls')),
	path('investisseurs/', include('investisseur.urls')),
	path('investissements/', include('investissement.urls')),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




