from django.core.management.base import BaseCommand
from urllib.parse import urljoin
from django.conf import settings
import requests
import telebot
from decouple import config
from datetime import datetime


class Command(BaseCommand):
    help = 'Пример загрузки данных через REST API'

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', dest='username', help='Имя пользователя')
        parser.add_argument('--password', '-p', dest='password')
        # python3 manage.py runbot -u user_example -p 12345678

    def handle(self, *args, **options):    # команда для вызова: python3 manage.py runbot
        bot = telebot.TeleBot(config('TOKEN'))

        @bot.message_handler(commands=['start'])
        def start(message):
            bot.reply_to(message=message, text=f'Твой ID {message.chat.id}.\n'
                                               f'Сообщи его менеджеру и он тебя зарегистрирует')

        @bot.message_handler(commands=['start_day'])
        def start_day(message):
            pass

        @bot.message_handler(commands=['end_day'])
        def end_day(message):
            pass

        @bot.message_handler(commands=['end_order'])
        def end_order(message):
            pass

        while True:
            try:
                bot.polling()
            except Exception as error:
                initial_text = f"{error.__class__}\n{error}\n\n{datetime.now()}"
                txt = f"https://api.telegram.org/bot" \
                      f"{config('TOKEN')}/sendMessage?" \
                      f"chat_id={config('ADMIN_ID')}&" \
                      f"text={initial_text}"
                requests.get(txt)


