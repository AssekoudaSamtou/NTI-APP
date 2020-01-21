from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

from commerciaux.models import Commercial
from investisseur.models import Investisseur
from tradeur.models import Tradeur

TEMPLATES = {
    'investisseur': 'investisseur/espace/index.html',
    'tradeur': 'tradeur/espace/index.html',
    'commercial': 'commerciaux/espace/index.html',
}

def home(request):
    context = {}
    print(request.user.groups.all())
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_superuser:
        return render(request, 'dashboard.html', context)

    groups = request.user.groups.all()
    if len(groups) >= 1:
        if groups[0].name == 'investisseur':

            return redirect('espace_investisseur')

        if groups[0].name == 'tradeur':
            context['tradeur'] = Tradeur.objects.get(id=request.user.id)
            return render(request, TEMPLATES['tradeur'], context)

        if groups[0].name == 'commercial':
            context['investisseur'] = Commercial.objects.get(id=request.user.id)
            return render(request, TEMPLATES['commerciaux'], context)
    raise Http404(request)


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
