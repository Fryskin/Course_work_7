import logging

from celery import shared_task

import json
from datetime import datetime, timedelta
from celery.worker.state import requests
from django.conf import settings
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from useful_habits.models import UsefulHabit
from users.models import User

# schedule, created = IntervalSchedule.objects.get_or_create(
#      every=10,
#      period=IntervalSchedule.SECONDS,
#  )
#
# PeriodicTask.objects.create(
#      interval=schedule,
#      name='Importing contacts',
#      task='useful_habits.tasks.request_telegram_names',
#      expires=datetime.utcnow() + timedelta(seconds=30)
#  )
#
# PeriodicTask.objects.create(
#      interval=schedule,
#      name='Importing contacts',
#      task='useful_habits.tasks.request_telegram_names',
#      expires=datetime.utcnow() + timedelta(seconds=30)
#  )

@shared_task
def request_telegram_names():
    """ Scanning the telegram bot and associate usernames with chat_id"""
    telegram_users = User.objects.all()
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/getUpdates"
    response = requests.get(url)
    updated_data = response.json()['result']
    for updated_tlg in updated_data:
        for telegram_base in telegram_users:
            if telegram_base.telegram_id == updated_tlg['message']['from'].get('username'):
                telegram_base.chat_id = updated_tlg['message']['chat']['id']
                telegram_base.save()


@shared_task
def remind(self, *args, **options):
    for useful_habit in UsefulHabit.objects.all():
        logging.info(f'Now Im able to send {useful_habit} to tlg_id {useful_habit.owner.telegram_id}')
        message = f'I remind you that at {useful_habit.time}' \
                  f'you supposed to do {useful_habit.action} in {useful_habit.location}.'
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage" \
              f"?chat_id={useful_habit.owner.chat_id}&text={message}"
        response = requests.get(url)
        logging.info(f"API response is: {response.status_code}")