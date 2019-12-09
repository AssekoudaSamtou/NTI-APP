from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'broker/index.html', context)
