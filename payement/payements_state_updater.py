from datetime import date

# from apscheduler.schedulers.background import BackgroundScheduler
#
# scheduler = BackgroundScheduler()

# @scheduler.scheduled_job('cron', day_of_week='*', hour=23, minute=33)
# @scheduler.scheduled_job('interval', seconds=30)
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


# sched.add_job(refresh_status_job, 'cron', day_of_week='*', hour=23, minute=21)


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')


# scheduler.start()
# scheduler.shutdown(wait=False)
