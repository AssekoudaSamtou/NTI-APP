from datetime import date

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.db.models import QuerySet
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

from password_generator import PasswordGenerator

from investissement.models import Investissement
from investissement.utils import incrementer_date
from investisseur.forms import InvestisseurForm
from investisseur.models import Investisseur
from payement.models import Payement

pwo = PasswordGenerator()

@login_required
@staff_member_required
def index(request):
    context = {
        "investisseurs": Investisseur.objects.all()
    }
    return render(request, 'investisseur/index.html', context)


@login_required
@staff_member_required
def ajouter(request):
    form = InvestisseurForm()
    context = {'form': form}
    if request.method == 'POST':
        form = InvestisseurForm(request.POST)
        print(form.errors)
        print(request.POST['username'])
        print(form.is_valid())
        if form.is_valid():
            first_password = pwo.generate()
            print(first_password)
            investisseur = form.save()
            investisseur.password = make_password(first_password)
            investisseur.init_password = first_password
            investisseur.save()
            investisseur_grp = Group.objects.get(name="investisseur")
            investisseur_grp.user_set.add(investisseur)

            return redirect('investisseurs')

    return render(request, 'investisseur/ajouter.html', context)


@login_required
@staff_member_required
def modifier(request, pk):
    investisseur = Investisseur.objects.get(id=pk)
    form = InvestisseurForm(
        initial={
            'first_name': investisseur.first_name,
            'last_name': investisseur.last_name,
            'email': investisseur.email,
            'telephone': investisseur.telephone,
            'sexe': investisseur.sexe,
        }
    )
    context = {
        'form': form,
        'investisseur': investisseur,
    }
    if request.method == 'POST':
        form = InvestisseurForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print('is valid')
            if form.has_changed():
                print('has changed')
                investisseur.first_name = request.POST['nom']
                investisseur.last_name = request.POST['prenom']
                investisseur.email = request.POST['email']
                investisseur.telephone = request.POST['telephone']
                investisseur.sexe = request.POST['sexe']
                investisseur.save()
                return redirect('investisseurs')

    return render(request, 'investisseur/modifier.html', context)


@login_required
@staff_member_required
def supprimer(request, pk):
    investisseur = Investisseur.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            investisseur.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            investisseur.delete()
            return redirect('investisseurs')
        return redirect('investisseurs')


@login_required
def espace(request):
    try:
        user = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    investissements = user.investissements.all()
    payements = Payement.objects.filter(investissement__investisseur=user)
    context = {
        'investisseur': user,
        'investissements_en_cours': [i for i in investissements if not i.is_finish()],
        'somme_investissements': sum(i.montant for i in investissements if not i.is_finish()),
        'investissements_termine': [i for i in investissements if i.is_finish()],
        'nb_virements': len([p for p in payements if p.status == "VR"]), #Virement effetuer
        'gains': sum([p.montant for p in payements if p.status == "NP"])
    }

    return render(request, 'investisseur/espace/index.html', context)


@login_required
def liste_investissements(request):
    try:
        user = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    investissements = user.investissements.all()
    encours = [i for i in investissements if incrementer_date(i.date_decompte, 30*i.duree) > date.today()]

    context = {
        'encours': encours,
        'investissements': investissements,
    }

    return render(request, 'investisseur/espace/investissements/liste.html', context=context)
