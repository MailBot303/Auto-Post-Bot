import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store video categories and their corresponding groups
categories = {
    'Category 1': {'group_id': 'GROUP_ID_1', 'videos': ['video1.mp4', 'video2.mp4', 'video3.mp4']},
    'Category 2': {'group_id': 'GROUP_ID_2', 'videos': ['video4.mp4', 'video5.mp4', 'video6.mp4']},
    'Category 3': {'group_id': 'GROUP_ID_3', 'videos': ['video7.mp4', 'video8.mp4', 'video9.mp4']}
}

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    # Customizable text to send when the bot starts
    start_text = "Welcome to the Video Bot!\n\nPlease choose an action:"

    # Inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("Force Subscribe", url="https://t.me/testgroup6999")],
        [InlineKeyboardButton("Custom Link", url="https://t.me/testgroup6999")],
        [InlineKeyboardButton("Verify", callback_data="verify")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the welcome message with inline keyboard
    if update.message:
        update.message.reply_text(start_text, reply_markup=reply_markup)
    else:
        update.callback_query.message.reply_text(start_text, reply_markup=reply_markup)

# Function to handle category button clicks
def category_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    category = query.data
    if category in categories:
        category_info = categories[category]
        group_id = category_info['group_id']
        video = random.choice(category_info['videos'])
        context.bot.forward_message(chat_id=query.message.chat_id, from_chat_id=group_id, message_id=video)

# Function to handle verify button clicks
def verify_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user = query.from_user
    group_id = "-1002023129341"  # Replace with your group ID
    if context.bot.get_chat_member(group_id, user.id).status == "member":
        # User is in the group, send the category list
        keyboard = [[InlineKeyboardButton(category, callback_data=category)] for category in categories.keys()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("Please choose a category:", reply_markup=reply_markup)
    else:
        # User is not in the group, prompt them to join the group
        query.answer("You are not a member of the group. Please join the group to proceed.")

# Function to handle all other messages
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Please use the provided buttons to interact with the bot.")

# Main function
def main() -> None:
    # Set up the Telegram Bot
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher

    # Define handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(category_callback, pattern='^Category'))
    dispatcher.add_handler(CallbackQueryHandler(verify_callback, pattern='^verify$'))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
