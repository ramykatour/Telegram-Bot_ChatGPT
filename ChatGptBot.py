import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
openai.api_key = "Your_OpenAi_API"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm a Katour bot powered by AI. How can I assist you?")

# Define a message handler for text messages
def echo(update, context):
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=update.message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Send the response back to the user
    context.bot.send_message(chat_id=update.message.chat_id, text=response.choices[0].text)

def main():
    # Create the Telegram bot and attach a message handler to it
    updater = Updater(token="Your_Telegram_Token_from_BotFather", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
