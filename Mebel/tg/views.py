from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyMarkup
from tg.globals import TEXTS
from tg.models import Log, TgUser
from mebel_sayt.models import *


def btns(type=None, lang=1):
    btn = []
    if type == 'menu':
        btn = [
            [KeyboardButton(TEXTS['BTN_CTG'][lang]), KeyboardButton(TEXTS['BTN_SETTINGS'][lang])]
        ]
    else:
        btn = [
            [KeyboardButton('Uz'), KeyboardButton('Ru'), KeyboardButton("En")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.message = {'state': 0}
        tglog.save()
    log = tglog.message
    tg_user = TgUser.objects.filter(user_id=user.id).first()

    if not tg_user:
        tg_user = TgUser()
        tg_user.user_id = user.id
        tg_user.user_name = user.username
        tg_user.save()

    tg_user.menu_log = 0
    tg_user.save()
    log['state'] = 0
    tglog.message = log
    tglog.save()
    if not tg_user.lang:
        update.message.reply_text(TEXTS['START'], reply_markup=btns())
    else:
        update.message.reply_text(TEXTS['MENU'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        log['state'] = 10
        tglog.message = log
        tglog.save()


def message_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = TgUser.objects.filter(user_id=user.id).first()
    log = tglog.message
    msg = update.message.text
    state = log.get('state', 0)
    if msg == '@admin':
        update.message.reply_text(['AdminPass'][tg_user.lang])
        log['admin_state'] = 0

        tglog.message = log
        tglog.save()
        return 0
    elif log.get('admin_state') == 0:
        if msg == '12345':
            tg_user.menu = 1
            tg_user.save()
            log.clear()
            log['admin_state'] = 1
            tglog.message = log
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['invalid'][tg_user.lang])
            return 0

    if state == 0:
        log['state'] = 1
        if msg == 'Uz':
            tg_user.lang = 1
            tg_user.save()
        elif msg == 'Ru':
            tg_user.lang = 2
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns())
            return 0
        update.message.reply_text(TEXTS['MENU'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        tglog.message = log
        tglog.save()


