from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.db import transaction
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from password_generator import PasswordGenerator

from investisseur.forms import InvestisseurForm, InvestisseurFormDisabled
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
@transaction.atomic
def ajouter(request):
    form = InvestisseurForm()
    context = {'form': form}

    if request.method == 'POST':
        form = InvestisseurForm(request.POST)

        if form.is_valid():
            first_password = pwo.generate()
            investisseur = form.save()
            investisseur.password = make_password(first_password)
            investisseur.init_password = first_password
            investisseur.save()

            try:
                investisseur_grp = Group.objects.get(name="investisseur")
                investisseur_grp.user_set.add(investisseur)
            except Group.DoesNotExist:
                create_end_user_groups()

            return redirect('investisseurs')

    return render(request, 'investisseur/ajouter.html', context)


def ajouter_investissement(request):
    pass

@login_required
@staff_member_required
@transaction.atomic
def modifier(request, pk):
    investisseur = Investisseur.objects.get(id=pk)
    groups = request.user.groups.all()
    # if len(groups) >= 1 and groups[0].name == 'caissier':

    form = InvestisseurForm(
        initial={
            'first_name': investisseur.first_name,
            'last_name': investisseur.last_name,
            'username': investisseur.username,
            'email': investisseur.email,
            'telephone': investisseur.telephone,
            'sexe': investisseur.sexe,
        }
    )
    context = {
        'form': form,
        'investisseur': investisseur,
        'can__delete': request.user.is_superuser,
        'can__add_investissement': request.user.is_superuser or groups[0].name == "caissier",
    }
    if request.method == 'POST':
        form = InvestisseurForm(request.POST, request.FILES)
        print(form.errors)
        # if form.is_valid():
        if form.has_changed():
            print('has changed')
            investisseur.first_name = request.POST['first_name']
            investisseur.last_name = request.POST['last_name']
            investisseur.email = request.POST['email']
            investisseur.telephone = request.POST['telephone']
            investisseur.sexe = request.POST['sexe']
            investisseur.save()
            return redirect('investisseurs')

    return render(request, 'investisseur/modifier.html', context)


@login_required
@staff_member_required
@transaction.atomic
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
        # 'investisseur': user,
        'investissements_en_cours': [i for i in investissements if not i.is_finish()],
        'investissements': investissements,
        'somme_investissements': sum(i.montant for i in investissements),
        'investissements_termine': [i for i in investissements if i.is_finish()],
        'nb_virements': len([p for p in payements if p.status == "VR"]),  # Virement effetuer
        'gains': sum([p.montant for p in payements if p.status == "EC"])
    }

    return render(request, 'investisseur/espace/index.html', context)


@login_required
def liste_investissements(request):
    try:
        user = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    investissements = user.investissements.all()

    context = {
        'investissements': investissements,
    }

    return render(request, 'investisseur/espace/investissements/liste.html', context=context)


@login_required
def liste_filleuls(request):
    try:
        user = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    context = {
        'filleuls': Investisseur.objects.filter(parrain=user)
    }
    return render(request, 'investisseur/espace/filleuls/liste.html', context=context)

@login_required
def liste_payements(request):
    try:
        user = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    investissements = user.investissements.all()

    context = {
        'investissements': investissements,
    }

    return render(request, 'investisseur/espace/payements/liste.html', context=context)


def create_end_user_groups():
    grps = Group.objects.all()
    for g in grps:
        g.delete()

    Group(name="tradeur").save()
    Group(name="investisseur").save()
    Group(name="commercial").save()
