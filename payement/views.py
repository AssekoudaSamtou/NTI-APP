from django.http import JsonResponse
from django.shortcuts import render, redirect

from payement.forms import PayementForm
from payement.models import Payement


def index(request):
    context = {
        "payements": Payement.objects.all()
    }
    return render(request, 'payement/index.html', context)

def ajouter(request):
    form = PayementForm()
    context = {'form': form}
    if request.method == 'POST':
        form = PayementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('payements')

    return render(request, 'payement/ajouter.html', context)


def modifier(request, pk):
    payement = Payement.objects.get(id=pk)
    form = PayementForm(
        initial={
            'investissement': payement.investissement,
            'date': payement.date.strftime('%Y-%m-%d'),
            'montant': payement.montant,
            'status': payement.status,
        }
    )
    context = {
        'form': form,
        'payement': payement,
    }
    if request.method == 'POST':
        form = PayementForm(request.POST)
        form.instance = payement
        print(form.errors)
        if form.is_valid():
            print('is valid')
            if form.has_changed():
                print('has changed')
                form.save()
                return redirect('payements')

    return render(request, 'payement/modifier.html', context)


def supprimer(request, pk):
    payement = Payement.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            payement.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            payement.delete()
            return redirect('payements')
        return redirect('payements')