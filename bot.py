import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store video categories and their corresponding lists of videos
categories = {
    'Category 1': ['video1.mp4', 'video2.mp4', 'video3.mp4'],
    'Category 2': ['video4.mp4', 'video5.mp4', 'video6.mp4'],
    'Category 3': ['video7.mp4', 'video8.mp4', 'video9.mp4']
}

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(category, callback_data=category)] for category in categories.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose a category:', reply_markup=reply_markup)

# Function to handle category button clicks
def category_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    category = query.data
    video = random.choice(categories[category])
    context.bot.send_video(chat_id=query.message.chat_id, video=open(video, 'rb'))

# Main function
def main() -> None:
    # Set up the Telegram Bot
    updater = Updater("7148632757:AAFzYQ3eIQQg_TbKB50nLlTip8QjAVGkow4")
    dispatcher = updater.dispatcher

    # Define handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(category_callback))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
