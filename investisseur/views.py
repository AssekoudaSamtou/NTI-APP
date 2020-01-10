from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect

from password_generator import PasswordGenerator

from investisseur.forms import InvestisseurForm
from investisseur.models import Investisseur


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
        print(request.POST['parrain'])
        if form.is_valid():
            Investisseur.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                sexe=request.POST['sexe'],
                password=make_password(pwo.generate()),
            )
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
    context = {}
    context['investisseur'] = Investisseur.objects.get(id=request.user.id)
    return render(request, 'investisseur/espace/index.html', context)
