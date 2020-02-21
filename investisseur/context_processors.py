from investisseur.models import Investisseur


def infos_investisseur(request):
    try:
        investisseur = Investisseur.objects.get(id=request.user.id)
    except Investisseur.DoesNotExist:
        investisseur = None

    context = {'investisseur': investisseur}
    return context
