import traceback
from typing import Final

from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Application,CommandHandler,MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from Translator import t
import logging
from joblist import job_list_command
from models.User import User
load_dotenv()


TOKEN: Final = os.getenv('TELEGRAM_TOKEN')
BOT_USERNAME: Final = os.getenv('TELEGRAM_LINK')

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # set buttons
    buttons = [
        [KeyboardButton('🔎 List Jobs')],
        [KeyboardButton('🔔 Set notifications'), KeyboardButton('🏢 List companies')],
        [KeyboardButton('❓ Help'), KeyboardButton('🔙 Back')]
    ]
    # create markup
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    try:
        User.create({
            'id': update.message.from_user.id,
            'username': update.message.from_user.username,
            'first_name': update.message.from_user.first_name,
            'last_name': update.message.from_user.last_name,
            'language_code': update.message.from_user.language_code
        })
    except Exception as e:
        traceback.print_exc()

    await update.message.reply_markdown(t('start message', update.message.from_user.language_code), reply_markup=markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(t('help message'))

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(t('settings message'))

# Connect job_list_command from joblist.py
async def list_jobs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await job_list_command(update, context)

async def set_notifications_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(t('set notifications message'))

async def list_companies_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(t('list companies message'))

# Handle Responses
def handle_response(txt: str) -> str:
    processed: str = txt.lower()

    if 'hello' in processed:
        return 'Hey there!'
    if '🔎 list jobs' in processed:
        return 'I am good!'
    return 'I do not understand what your wrote :('

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text is None:
        return
    elif text == '🔎 List Jobs':
        return await list_jobs_command(update, context)
    elif text == '🔔 Set notifications':
        return await set_notifications_command(update, context)
    elif text == '🏢 List companies':
        return await list_companies_command(update, context)
    elif text == '❓ Help':
        return await help_command(update, context)
    elif text == '🔙 Back':
        return await start_command(update, context)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('settings', settings_command))

    # Handle the /listjobs command
    app.add_handler(CommandHandler('listjobs', list_jobs_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
