from datetime import date

def refresh_status_job():
    from .models import Payement

    print('This job is run every 1 minutes.')

    payements = list(Payement.objects.filter(status="NP")) + list(Payement.objects.filter(status=None))

    for payement in payements:
        if payement.date < date.today():
            payement.status = "EC"
            payement.save()
        elif payement.debut_payement() < date.today():
            payement.status = "NP"
            payement.save()
