from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'investisseur/index.html', context)
