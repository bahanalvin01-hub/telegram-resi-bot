import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# List of courier services
COURIERS = {
    'jne': 'https://api.jne.co.id/',
    'pos': 'https://api.posindonesia.co.id/',
    'tiki': 'https://api.tiki.id/',
    'sicepat': 'https://api.sicepat.com/',
    'lion': 'https://api.lionexpress.com/'
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your tracking bot. Use /help to get the list of commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/start - Start the bot\n/help - Get help\n/tracking <courier> <tracking_number> - Check package status')

def tracking(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 2:
        update.message.reply_text('Usage: /tracking <courier> <tracking_number>')
        return

    courier = context.args[0].lower()
    tracking_number = context.args[1]

    if courier not in COURIERS:
        update.message.reply_text('Supported couriers: ' + ', '.join(COURIERS.keys()))
        return

    # Replace with actual API call
    response = requests.get(f'{COURIERS[courier]}/track/{tracking_number}')
    if response.status_code == 200:
        data = response.json()
        update.message.reply_text(f'Tracking information: {data}')
    else:
        update.message.reply_text('Tracking information not found. Please check the tracking number.')

def main() -> None:
    updater = Updater('YOUR_API_KEY')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('tracking', tracking))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()