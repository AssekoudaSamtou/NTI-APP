from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from accounts.forms import UpdateInfosPersoForm, UpdateContactForm, UpdatePasswordForm
from investisseur.models import Investisseur


@login_required
def view_profile(request):
    try:
        investisseur = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    args = {
        'user': investisseur,
        'infoForm': UpdateInfosPersoForm(
            initial={
                'first_name': investisseur.first_name,
                'last_name': investisseur.last_name,
                'username': investisseur.username,
            }
        ),
        'contactForm': UpdateContactForm(
            initial={
                'email': investisseur.email,
                'telephone': investisseur.telephone
            }
        )
    }
    return render(request, 'accounts/profile.html', args)

@login_required
def update_infos_perso(request):
    try:
        investisseur = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    if request.method == "POST":
        form = UpdateInfosPersoForm(request.POST)
        form.instance = investisseur
        print(form.errors)
        if form.is_valid():
            print("saved")
            form.save()
        return redirect('view_profile')
    else:
        raise Http404("Not Found")

@login_required
def update_contacts(request):
    try:
        investisseur = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    if request.method == "POST":
        form = UpdateContactForm(request.POST)
        form.instance = investisseur
        print(form.errors)
        if form.is_valid():
            print("saved")
            form.save()
        return redirect('view_profile')
    else:
        raise Http404("Not Found")

@login_required
def change_pwd(request):
    try:
        investisseur = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        raise Http404("Investisseur Not Found")

    if request.method == "POST":
        old_pwd = request.POST.get('old_pass')
        new_pwd = request.POST.get('new_pass')
        r_new_pwd = request.POST.get('r_new_pass')

        if check_password(old_pwd, investisseur.password) and new_pwd == r_new_pwd:
            investisseur.password = make_password(new_pwd)
            investisseur.save()
            print("password changed")
            return redirect('login')
    else:
        raise Http404("Not Found")
