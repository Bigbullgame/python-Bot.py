import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token from BotFather
TOKEN = "7873773189:AAGj3yq8cqlACKQIWT9tjHQkeHDSCozmTuc"

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am an echo bot. I will repeat any message sent in this group.')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # Don't echo if the message is from the bot itself to avoid infinite loops
    if update.message.from_user.id == context.bot.id:
        return
    
    # Get the original message text
    original_text = update.message.text
    
    # Only echo if there's actual text (not commands, photos, etc.)
    if original_text:
        # Send the echoed message
        update.message.reply_text(f"Echo: {original_text}")

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non-command messages - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
