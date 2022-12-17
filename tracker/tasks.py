from celery import shared_task
from datetime import datetime

@shared_task(name='print_msg')
def print_msg():
    print("Celery Beat is working!")

@shared_task(name='current_time')
def print_time():
    now = datetime.now()
    print(f"Current time: {now.strftime('%H:%M:%S')}")