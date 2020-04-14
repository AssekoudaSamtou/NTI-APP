from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from password_generator import PasswordGenerator

from tradeur.forms import TradeurForm
from tradeur.models import Tradeur

pwo = PasswordGenerator()


def index(request):
    context = {
        "tradeurs": Tradeur.objects.all()
    }
    return render(request, 'tradeur/index.html', context)

@login_required
@staff_member_required
@transaction.atomic
def ajouter(request):
    form = TradeurForm()
    context = {'form': form}

    if request.method == 'POST':
        form = TradeurForm(request.POST, request.FILES)

        if form.is_valid():
            first_password = pwo.generate()
            tradeur = form.save()
            tradeur.password = make_password(first_password)
            tradeur.init_password = first_password

            try:
                tradeur_grp = Group.objects.get(name="tradeur")
                tradeur_grp.user_set.add(tradeur)
            except Group.DoesNotExist:
                pass

        return redirect('tradeurs')

    return render(request, 'tradeur/ajouter.html', context)


@login_required
@staff_member_required
@transaction.atomic
def profile(request, pk):
    tradeur = Tradeur.objects.get(id=pk)
    form = TradeurForm(
        initial={
            'first_name': tradeur.first_name,
            'last_name': tradeur.last_name,
            'username': tradeur.username,
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

        print(form.errors)
        # if form.is_valid():
        if form.has_changed():
            print('has changed')
            tradeur.first_name = request.POST['first_name']
            tradeur.last_name = request.POST['last_name']
            tradeur.email = request.POST['email']
            tradeur.telephone = request.POST['telephone']
            tradeur.sexe = request.POST['sexe']
            if request.FILES.get('avatar'):
                tradeur.avatar = request.FILES.get('avatar')
            tradeur.save()
            return redirect('tradeurs')

    return render(request, 'tradeur/profile.html', context)


@login_required
@staff_member_required
@transaction.atomic
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
