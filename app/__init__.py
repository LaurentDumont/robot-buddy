from celery import Celery

def make_celery(app_name=__name__):
    broker = "pyamqp://"
    return Celery(app_name, broker=broker)

celery = make_celery()
