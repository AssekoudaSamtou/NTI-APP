from django.shortcuts import render, redirect

# Create your views here.
from tradeur.forms import TradeurForm
from tradeur.models import Tradeur


def home(request):
    context = {}
    return render(request, 'home.html', context)

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

        if form.is_valid():
            Tradeur.objects.create(
                nom=request.POST['nom'],
                prenom=request.POST['prenom'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                sexe=request.POST['sexe'],
                avatar=request.POST.get('avatar')
            )
            return redirect('tradeurs')

    return render(request, 'tradeur/ajouter.html', context)


def profile(request, pk):
    context = {}
    return render(request, 'tradeur/profile.html', context)