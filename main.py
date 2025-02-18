import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters
import openai

openai.api_key = "TvoyApi"

def generate_response(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your AI assistant. How can I help you today?")

def main():
    bot = telegram.Bot(token="TvoyTgToken")

    dispatcher = bot.dispatcher

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text & ~Filters.command, generate_response)
    dispatcher.add_handler(message_handler)

    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    main()







