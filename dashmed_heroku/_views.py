from django.http import Http404
from django.shortcuts import render, redirect

from commerciaux.models import Commercial
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


def handler404(request, exception):
    context = {}
    return render(request, "error/404.html", context=context)
