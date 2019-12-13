from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from investisseur.forms import InvestisseurForm
from investisseur.models import Investisseur


def index(request):
    context = {
        "investisseurs": Investisseur.objects.all()
    }
    return render(request, 'investisseur/index.html', context)


def ajouter(request):
    form = InvestisseurForm()
    context = {'form': form}
    if request.method == 'POST':
        form = InvestisseurForm(request.POST)

        if form.is_valid():
            Investisseur.objects.create(
                nom=request.POST['nom'],
                prenom=request.POST['prenom'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                sexe=request.POST['sexe'],
            )
            return redirect('investisseurs')

    return render(request, 'investisseur/ajouter.html', context)


def modifier(request, pk):
    investisseur = Investisseur.objects.get(id=pk)
    form = InvestisseurForm(
        initial={
            'nom': investisseur.nom,
            'prenom': investisseur.prenom,
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
                investisseur.nom = request.POST['nom']
                investisseur.prenom = request.POST['prenom']
                investisseur.email = request.POST['email']
                investisseur.telephone = request.POST['telephone']
                investisseur.sexe = request.POST['sexe']
                investisseur.save()
                return redirect('investisseurs')

    return render(request, 'investisseur/modifier.html', context)


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