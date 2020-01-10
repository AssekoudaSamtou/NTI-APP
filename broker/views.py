from django.http import JsonResponse
from django.shortcuts import render, redirect

from broker.forms import BrokerForm
from broker.models import Broker


def index(request):
    context = {
        "brokers": Broker.objects.all()
    }
    return render(request, 'broker/index.html', context)


def ajouter(request):
    form = BrokerForm()
    context = {'form': form}
    if request.method == 'POST':
        form = BrokerForm(request.POST)

        if form.is_valid():
            Broker.objects.create(
                libelle=request.POST['libelle'],
                site_web=request.POST['site_web'],
            )
            return redirect('brokers')

    return render(request, 'broker/ajouter.html', context)


def modifier(request, pk):
    broker = Broker.objects.get(id=pk)
    form = BrokerForm(
        initial={
            'libelle': broker.libelle,
            'site_web': broker.site_web,
        }
    )
    context = {
        'form': form,
        'broker': broker,
    }
    if request.method == 'POST':
        form = BrokerForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('is valid')
            if form.has_changed():
                print('has changed')
                broker.libelle = request.POST['libelle']
                broker.site_web = request.POST['site_web']
                broker.save()
                return redirect('brokers')

    return render(request, 'broker/modifier.html', context)


def supprimer(request, pk):
    broker = Broker.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            broker.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            broker.delete()
            return redirect('brokers')
        return redirect('brokers')
