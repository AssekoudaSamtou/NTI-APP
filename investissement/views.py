from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, reverse

from investissement.forms import InvestissementForm, InvestissementForm2
from investissement.models import Investissement
from investisseur.models import Investisseur

from datetime import date


@login_required
@staff_member_required
def index(request):
    groups = request.user.groups.all()

    if request.user.is_superuser:
        investissements = Investissement.objects.all()
    elif groups[0].name == "caissier":
        investissements = Investissement.objects.filter(date_investissement=date.today())
    else:
        raise Http404(request)

    context = {
        "investissements": investissements
    }
    return render(request, 'investissement/index.html', context)

@login_required
@staff_member_required
@transaction.atomic
def ajouter(request, pk=None):
    form = InvestissementForm()
    if pk:
        form = InvestissementForm2(
            initial={
                'investisseur': Investisseur.objects.get(pk=pk),
            }
        )

    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = InvestissementForm(request.POST)
        print(form.errors)
        if form.is_valid():
            investissement = form.save()

            # investissement.generer_payements()

            return redirect('investissements')

    return render(request, 'investissement/ajouter.html', context)


@login_required
@staff_member_required
@transaction.atomic
def modifier(request, pk):
    investissement = Investissement.objects.get(id=pk)
    form = InvestissementForm(
        initial={
            'investisseur': investissement.investisseur,
            'montant': investissement.montant,
            'date_investissement': investissement.date_investissement.strftime('%Y-%m-%d'),
            'date_decompte': investissement.date_decompte.strftime('%Y-%m-%d'),
            'duree': investissement.pack.duree,
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


@login_required
@staff_member_required
@transaction.atomic
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


