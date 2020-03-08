from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from compte.models import Compte
from exercice.forms import ExerciceForm
from exercice.models import Exercice, ExerciceCompte


@login_required
@staff_member_required
def index(request):
    context = {
        "exercices": Exercice.objects.all()
    }
    return render(request, 'exercice/index.html', context)


@login_required
@staff_member_required
def ajouter(request):
    form = ExerciceForm()
    context = {
        'form': form,
        'comptes': Compte.objects.all(),
    }
    if request.method == 'POST':
        form = ExerciceForm(request.POST)
        comptes = request.POST.getlist("comptes")

        exercice = Exercice(
            nom=request.POST["nom"],
            date_debut=request.POST["date_debut"],
            duree=request.POST["duree"],
            balance_initialisation=request.POST["balance_initialisation"],
            objectif=request.POST["objectif"],
        )
        exercice.save()
        for compte in comptes:
            ExerciceCompte(exercice=exercice, compte=Compte.objects.get(id=int(compte))).save()

        return redirect('exercices')

    return render(request, 'exercice/ajouter.html', context)


@login_required
@staff_member_required
def modifier(request, pk):
    exercice = Exercice.objects.get(id=pk)

    form = ExerciceForm(
        initial={
            'nom': exercice.nom,
            'date_debut': exercice.date_debut,
            'duree': exercice.duree,
            'balance_initialisation': exercice.balance_initialisation,
            'objectif': exercice.objectif
        }
    )
    context = {
        'form': form,
        'exercice': exercice,
        'comptes': Compte.objects.all(),
    }
    if request.method == 'POST':
        form = ExerciceForm(request.POST)

        # if form.is_valid():
        if form.has_changed():
            exercice.nom = request.POST['nom']
            exercice.date_debut = request.POST['date_debut']
            exercice.duree = request.POST['duree']
            exercice.balance_initialisation = request.POST['balance_initialisation']
            exercice.objectif = request.POST['objectif']

            exercice.save()

            data = ExerciceCompte.objects.filter(exercice=exercice)
            for ec in data: ec.delete()

            comptes = request.POST.getlist("comptes")
            for compte in comptes:
                ExerciceCompte(exercice=exercice, compte=Compte.objects.get(id=int(compte))).save()

            return redirect('exercices')

    return render(request, 'exercice/modifier.html', context)


@login_required
@staff_member_required
def supprimer(request, pk):
    exercice = Exercice.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            exercice.delete()
            response = JsonResponse({"success": True})
            return response
    else:
        if request.method == "POST":
            exercice.delete()
            return redirect('exercices')
        return redirect('exercices')
