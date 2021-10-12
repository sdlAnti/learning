#from main import run_test
import json
from config import *
from reporting import *
import telegram
from telegram import Update, ForceReply, Chat
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime

def start(update: Update, context: CallbackContext) -> None:

    if str(update.message.chat.id) in TELEGRAM_CHAT_IDS:
        update.message.reply_text("Available commands: \n /start \n /status \n /adddomen \n /deldomen \n /domens \n /chat_id \ndomens available without http & https, like 'example.com'")
    else:
        update.message.reply_text('Sorry this bot only for personal use')

def status(update: Update, context: CallbackContext) -> None:
    if str(update.message.chat.id) in TELEGRAM_CHAT_IDS:
        with open('lastCheck.json', 'r') as f:
            dict1 = json.load(f)
        message = dict1['message']
        message = [message[i:i + 3000] for i in range(0, len(message), 3000)]
        for msg in message:
            update.message.reply_text(f"Last check was been in {dict1['last_check']}. \n Message: \n {msg}")

def adddomen(update: Update, context: CallbackContext) -> None:

    if str(update.message.chat.id) in TELEGRAM_CHAT_IDS:
        sites = []
        tmp = update.message.text.strip()
        tmp = tmp.replace('/adddomen','').strip()
        with open('pages_for_check.txt', 'a') as f:
            f.write('\n'+tmp)
        try:
            for el in TELEGRAM_CHAT_IDS:
                    send_telegram(el, f'Added {tmp} by {update.message.chat.username}')
        except:
            print('Failed with sending telegram message')

def deldomen(update: Update, context: CallbackContext) -> None:
    if str(update.message.chat.id) in TELEGRAM_CHAT_IDS:
        sites = []
        with open('pages_for_check.txt', 'r') as f:
            for line in f:
                sites.append(line.strip())
        tmp = update.message.text.strip()
        tmp = tmp.replace('/deldomen','').strip()
        sites.remove(tmp)
        with open('pages_for_check.txt', 'w') as f:
            for el in sites:
                f.write(el+'\n')
        try:
            for el in TELEGRAM_CHAT_IDS:
                    send_telegram(el, f'Deleted {tmp} by {update.message.chat.username}')
        except:
            print('Failed with sending telegram message')

def domens(update: Update, context: CallbackContext) -> None:
    if str(update.message.chat.id) in TELEGRAM_CHAT_IDS:
        sites = []
        with open('pages_for_check.txt', 'r') as f:
            for line in f:
                sites.append(line.strip())
        tmp = 'I looking for this sites:\n'
        for el in sites:
            tmp += el+'\n'
        update.message.reply_text(tmp)

def chat_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(str(update.message.chat.id))

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("adddomen", adddomen))
    dispatcher.add_handler(CommandHandler("deldomen", deldomen))
    dispatcher.add_handler(CommandHandler("domens", domens))
    dispatcher.add_handler(CommandHandler("chat_id", chat_id))



    # on non command i.e message - echo the message on Telegram


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()