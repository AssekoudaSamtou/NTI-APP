from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'investissement/index.html', context)


def ajouter(request):
    return None


def modifier(request):
    return None