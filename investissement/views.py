from django.http import JsonResponse
from django.shortcuts import render, redirect

from investissement.forms import InvestissementForm
from investissement.models import Investissement
from payement.models import Payement

from datetime import datetime


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

            for i in range(investissement.duree):

                if i + 1 == investissement.duree:
                    montant_payement = float(investissement.montant) * 1.4
                else:
                    montant_payement = float(investissement.montant) * 0.4

                payement = Payement(
                    investissement=investissement,
                    date=incrementer_date(investissement.date_decompte, i+1),
                    montant=montant_payement
                )

                payement.investissement = investissement
                payement.save()

            return redirect('investissements')

    return render(request, 'investissement/ajouter.html', context)


def modifier(request, pk):
    investissement = Investissement.objects.get(id=pk)
    form = InvestissementForm(
        initial={
            'investisseur'       : investissement.investisseur,
            'montant'            : investissement.montant,
            'date_investissement': investissement.date_investissement.strftime('%Y-%m-%d'),
            'date_decompte'      : investissement.date_decompte.strftime('%Y-%m-%d'),
            'duree'              : investissement.duree,
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
                form.save()
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


def incrementer_date(date, increment):
    if date.month == 12:
        return datetime.strptime(f"{date.year+increment}-{increment}-{date.day}", '%Y-%m-%d')
    else:
        return datetime.strptime(f"{date.year}-{date.month+increment}-{date.day}", '%Y-%m-%d')
