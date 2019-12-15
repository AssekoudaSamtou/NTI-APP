from django.http import JsonResponse
from django.shortcuts import render, redirect

from compte.forms import CompteForm
from compte.models import Compte
from tradeur.models import Tradeur


def index(request):
    context = {
        "comptes": Compte.objects.all()
    }
    return render(request, 'compte/index.html', context)


def ajouter(request):
    form = CompteForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = CompteForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('comptes')

    return render(request, 'compte/ajouter.html', context)


def modifier(request, pk):
    compte = Compte.objects.get(id=pk)
    form = CompteForm(
        initial={
            'num_compte': compte.num_compte,
            'tradeur': compte.tradeur,
            'broker': compte.broker,
            'montant_investi': compte.montant_investi,
            'date_creation': compte.date_creation,
        }
    )
    form.instance = compte
    context = {
        'form': form,
        'compte': compte,
    }
    if request.method == 'POST':
        form = CompteForm(request.POST)
        form.instance = compte
        print(form.errors)
        if form.is_valid():
            if form.has_changed():
                form.save()
                return redirect('comptes')

    return render(request, 'compte/modifier.html', context)


def supprimer(request, pk):
    compte = Compte.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            compte.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            compte.delete()
            return redirect('comptes')
        return redirect('comptes')