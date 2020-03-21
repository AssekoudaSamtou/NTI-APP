from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from broker.models import Broker
from tradeur.forms import TradeurForm
from tradeur.models import Tradeur


def index(request):
    context = {
        "tradeurs": Tradeur.objects.all()
    }
    return render(request, 'tradeur/index.html', context)


def ajouter(request):
    form = TradeurForm()
    context = {'form': form}
    if request.method == 'POST':
        form = TradeurForm(request.POST, request.FILES)
        print(form.errors)
        # if form.is_valid():
        tradeur = Tradeur(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            sexe=request.POST['sexe']
        )
        if request.FILES.get('avatar'):
            tradeur.avatar = request.FILES.get('avatar')
        tradeur.save()
        return redirect('tradeurs')

    return render(request, 'tradeur/ajouter.html', context)


def profile(request, pk):
    tradeur = Tradeur.objects.get(id=pk)
    form = TradeurForm(
        initial={
            'nom': tradeur.first_name,
            'prenom': tradeur.last_name,
            'email': tradeur.email,
            'telephone': tradeur.telephone,
            'sexe': tradeur.sexe,
            'avatar': tradeur.avatar
        }
    )
    context = {
        'form': form,
        'tradeur': tradeur,
    }
    if request.method == 'POST':
        form = TradeurForm(request.POST, request.FILES)

        if form.is_valid():
            if form.has_changed():
                tradeur.first_name=request.POST['nom']
                tradeur.last_name=request.POST['prenom']
                tradeur.email=request.POST['email']
                tradeur.telephone=request.POST['telephone']
                tradeur.sexe=request.POST['sexe']
                if request.FILES.get('avatar'):
                    tradeur.avatar=request.FILES.get('avatar')
                tradeur.save()
                return redirect('tradeurs')

    return render(request, 'tradeur/profile.html', context)

def supprimer(request, pk):
    tradeur = Tradeur.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            tradeur.delete()
            response = JsonResponse({"success": True})
            return response
    else:
        if request.method == "POST":
            tradeur.delete()
            return redirect('tradeurs')
        return redirect('tradeurs')
