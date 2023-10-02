import logging

import requests
from django.conf import settings
from django.core.management import BaseCommand

from useful_habits.models import UsefulHabit
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        telegram_users = User.objects.all()
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/getUpdates"
        response = requests.get(url)
        updated_data = response.json()['result']
        for updated_tlg in updated_data:
            for telegram_base in telegram_users:
                if telegram_base.telegram_id == updated_tlg['message']['from'].get('username'):
                    telegram_base.chat_id = updated_tlg['message']['chat']['id']
                    telegram_base.save()

        for useful_habit in UsefulHabit.objects.all():
            logging.info(f'Now Im able to send {useful_habit} to tlg_id {useful_habit.owner.telegram_id}')
            message = f'I remind you that at {useful_habit.time}' \
                      f'you supposed to do {useful_habit.action} in {useful_habit.location}.'
            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage" \
                  f"?chat_id={useful_habit.owner.chat_id}&text={message}"
            response = requests.get(url)
            logging.info(f"API response is: {response.status_code}")


