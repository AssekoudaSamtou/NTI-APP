from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'operation/index.html', context)
