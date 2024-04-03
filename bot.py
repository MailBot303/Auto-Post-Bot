import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Define your video URLs for each category
category_videos = {
    "Funny Videos": [
        "https://www.example.com/funny_video1",
        "https://www.example.com/funny_video2",
        "https://www.example.com/funny_video3"
    ],
    "Educational Videos": [
        "https://www.example.com/educational_video1",
        "https://www.example.com/educational_video2"
    ],
    "Music Videos": [
        "https://www.example.com/music_video1",
        "https://www.example.com/music_video2",
        "https://www.example.com/music_video3",
        "https://www.example.com/music_video4"
    ],
    # Add more categories and videos as needed
}

# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    buttons = [
        [InlineKeyboardButton(category, callback_data=category)] for category in category_videos.keys()
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Please choose a category:', reply_markup=reply_markup)

# Function to handle category button clicks
def category_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    category = query.data
    video_url = random.choice(category_videos[category])
    query.answer()
    query.message.reply_video(video_url)

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("7148632757:AAFzYQ3eIQQg_TbKB50nLlTip8QjAVGkow4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for commands
    dispatcher.add_handler(CommandHandler("start", start))

    # Add handler for category button clicks
    dispatcher.add_handler(CallbackQueryHandler(category_selection))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
