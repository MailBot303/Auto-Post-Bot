import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

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
    user = update.message.from_user
    # Customize the welcome message as needed
    welcome_message = f"Hello {user.first_name}! Welcome to the Video Bot.\n\nPlease choose an option:"
    keyboard = [
        [InlineKeyboardButton("Force Subscribe", url="https://t.me/testgroup6999")],
        [InlineKeyboardButton("Custom Link", url="https://t.me/testgroup6999")],
        [InlineKeyboardButton("Verify", callback_data="verify")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Function to handle category button clicks
def category_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    category = query.data
    video = random.choice(categories[category])
    context.bot.send_video(chat_id=query.message.chat_id, video=open(video, 'rb'))

# Function to handle verify button clicks
def verify_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user = query.from_user
    group_id = -100123456789  # Replace with your group ID
    if user.id in context.bot.get_chat_member(group_id, user.id):
        start(update, context)  # Redirect to start function (show category menu)
    else:
        start(update, context)  # Resend the welcome message

# Main function
def main() -> None:
    # Set up the Telegram Bot
    updater = Updater("7148632757:AAFzYQ3eIQQg_TbKB50nLlTip8QjAVGkow4")
    dispatcher = updater.dispatcher

    # Define handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(category_callback))
    dispatcher.add_handler(CallbackQueryHandler(verify_callback))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
