from datetime import timedelta


def incrementer_date(date, increment):
    return date + timedelta(days=increment)
