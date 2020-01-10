from django.http import JsonResponse
from django.shortcuts import render, redirect

from investissement.forms import InvestissementForm
from investissement.models import Investissement
from payement.models import Payement

from datetime import timedelta


def index(request):
    context = {
        "investissements": Investissement.objects.all()
    }
    return render(request, 'investissement/index.html', context)


def ajouter(request):
    form = InvestissementForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = InvestissementForm(request.POST)
        print(form.errors)
        if form.is_valid():
            investissement = form.save()

            investissement.generer_payements()

            return redirect('investissements')

    return render(request, 'investissement/ajouter.html', context)


def modifier(request, pk):
    investissement = Investissement.objects.get(id=pk)
    form = InvestissementForm(
        initial={
            'investisseur': investissement.investisseur,
            'montant': investissement.montant,
            'date_investissement': investissement.date_investissement.strftime('%Y-%m-%d'),
            'date_decompte': investissement.date_decompte.strftime('%Y-%m-%d'),
            'duree': investissement.duree,
        }
    )
    form.instance = investissement
    context = {
        'form': form,
        'investissement': investissement,
    }
    if request.method == 'POST':
        form = InvestissementForm(request.POST)
        form.instance = investissement
        print(form.errors)
        if form.is_valid():
            if form.has_changed():
                investissement = form.save()
                investissement.supprimer_payements()
                investissement.generer_payements()

                return redirect('investissements')

    return render(request, 'investissement/modifier.html', context)


def supprimer(request, pk):
    investissement = Investissement.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            investissement.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            investissement.delete()
            return redirect('investissements')
        return redirect('investissements')


