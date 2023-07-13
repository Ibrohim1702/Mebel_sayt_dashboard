from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.core.management import BaseCommand

from Mebel.settings import TOKEN
from tg.views import message_handler, start


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(TOKEN)

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

        updater.start_polling()
        updater.idle()