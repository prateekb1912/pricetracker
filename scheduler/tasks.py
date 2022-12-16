from celery import shared_task

@shared_task(name = 'summary')
def send_notification():
    print('Here I am')
