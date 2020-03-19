#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from payement.payements_state_updater import refresh_status_job


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashmed_heroku.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_status_job, 'cron', day_of_week='*', hour=0, minute=1)
    scheduler.start()
    main()
    scheduler.shutdown(wait=False)
