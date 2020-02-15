from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from exercice.forms import ExerciceForm
from exercice.models import Exercice

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
    print(form.as_p())
    context = {'form': form}
    if request.method == 'POST':
        form = ExerciceForm(request.POST, request.FILES)
        print(form.errors)
        # if form.is_valid():
        exercice = Exercice(
            nom=request.POST['nom'],
            prenom=request.POST['prenom'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            sexe=request.POST['sexe']
        )
        exercice.save()
        return redirect('exercices')

    return render(request, 'exercice/ajouter.html', context)

@login_required
@staff_member_required
def modifier(request, pk):
    exercice = Exercice.objects.get(id=pk)
    form = ExerciceForm(
        initial={
            'nom': exercice.nom,
            'prenom': exercice.prenom,
            'email': exercice.email,
            'telephone': exercice.telephone,
            'sexe': exercice.sexe,
            'avatar': exercice.avatar
        }
    )
    context = {
        'form': form,
        'exercice': exercice,
    }
    if request.method == 'POST':
        form = ExerciceForm(request.POST, request.FILES)

        if form.is_valid():
            if form.has_changed():
                exercice.nom=request.POST['nom']
                exercice.prenom=request.POST['prenom']
                exercice.email=request.POST['email']
                exercice.telephone=request.POST['telephone']
                exercice.sexe=request.POST['sexe']
                if request.FILES.get('avatar'):
                    exercice.avatar=request.FILES.get('avatar')
                exercice.save()
                return redirect('exercices')

    return render(request, 'exercice/profile.html', context)

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

