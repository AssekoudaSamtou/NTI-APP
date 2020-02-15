from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from operation.forms import OperationForm
from operation.models import Operation

@login_required
@staff_member_required
def index(request):
    context = {
        "operations": Operation.objects.all()
    }
    return render(request, 'operation/index.html', context)


@login_required
@staff_member_required
def ajouter(request):
    form = OperationForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = OperationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # form.date
            form.save()
            return redirect('operations')

    return render(request, 'operation/ajouter.html', context)


@login_required
@staff_member_required
def modifier(request, pk):
    operation = Operation.objects.get(id=pk)
    print(operation.date.strftime('%Y-%m-%d'))
    form = OperationForm(
        initial={
            'date': operation.date.strftime('%Y-%m-%d'),
            'type_operation': operation.type_operation,
            'compte': operation.compte,
            'montant': operation.montant,
        }
    )
    form.instance = operation
    context = {
        'form': form,
        'operation': operation,
        'heure': operation.date.strftime('%H:%M'),
    }
    if request.method == 'POST':
        form = OperationForm(request.POST)
        form.instance = operation
        print(form.errors)
        if form.is_valid():
            if form.has_changed():
                form.save()
                if request.POST.get('heure'):
                    new_date = datetime.strptime(f"{request.POST['date']} {request.POST['heure']}:00", '%Y-%m-%d %H:%M:%S')
                    print(new_date)
                    operation.date = new_date
                    operation.save()
                return redirect('operations')

    return render(request, 'operation/modifier.html', context)


@login_required
@staff_member_required
def supprimer(request, pk):
    operation = Operation.objects.get(id=pk)

    if request.is_ajax():
        if request.method == "DELETE":
            operation.delete()
            return JsonResponse({"success": True})
    else:
        if request.method == "POST":
            operation.delete()
            return redirect('operations')
        return redirect('operations')
