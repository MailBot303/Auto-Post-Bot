from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Telegram Bot Token
TOKEN = '7148632757:AAFzYQ3eIQQg_TbKB50nLlTip8QjAVGkow4'

# Define the categories and corresponding video links
categories = {
    'Category 1': 'VIDEO_LINK_1',
    'Category 2': 'VIDEO_LINK_2',
    'Category 3': 'VIDEO_LINK_3',
    'Category 4': 'VIDEO_LINK_4',
    'Category 5': 'VIDEO_LINK_5',
    'Category 6': 'VIDEO_LINK_6',
    'Category 7': 'VIDEO_LINK_7',
}

# Start command handler
def start(update, context):
    keyboard = [
        [InlineKeyboardButton(category, callback_data=link)] for category, link in categories.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the video bot! Please select a category:', reply_markup=reply_markup)

# Callback query handler
def button(update, context):
    query = update.callback_query
    query.answer()
    query.message.reply_video(query.data)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
