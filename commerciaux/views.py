from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from commerciaux.forms import CommercialForm
from commerciaux.models import Commercial

@login_required
@staff_member_required
def index(request):
    context = {
        "commerciaux": Commercial.objects.all()
    }
    return render(request, 'commerciaux/index.html', context)

@login_required
@staff_member_required
def ajouter(request):
    form = CommercialForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CommercialForm(request.POST)

        if form.is_valid():
            Commercial.objects.create(
                nom=request.POST['nom'],
                prenom=request.POST['prenom'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                sexe=request.POST['sexe'],
            )
            return redirect('commerciaux')

    return render(request, 'commerciaux/ajouter.html', context)

@login_required
@staff_member_required
def modifier(request, pk):
    commercial = Commercial.objects.get(id=pk)
    form = CommercialForm(
        initial={
            'nom':       commercial.nom,
            'prenom':    commercial.prenom,
            'email':     commercial.email,
            'telephone': commercial.telephone,
            'sexe':      commercial.sexe,
        }
    )
    context = {
        'form': form,
        'commercial': commercial,
    }
    if request.method == 'POST':
        form = CommercialForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('is valid')
            if form.has_changed():
                print('has changed')
                commercial.nom = request.POST['nom']
                commercial.prenom = request.POST['prenom']
                commercial.email = request.POST['email']
                commercial.telephone = request.POST['telephone']
                commercial.sexe = request.POST['sexe']
                commercial.save()
                return redirect('commerciaux')

    return render(request, 'commerciaux/modifier.html', context)

@login_required
@staff_member_required
def supprimer(request, pk):
    commercial = Commercial.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            commercial.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            commercial.delete()
            return redirect('commerciaux')
        return redirect('commerciaux')
