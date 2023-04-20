import telegram

bot = telegram.Bot(token='BOT_TOKEN')

def replace_letter(update, context):
    text = update.message.text
    replaced_text = text.replace('a', 'b')
    bot.send_message(chat_id=update.message.chat_id, text=replaced_text)

from telegram.ext import MessageHandler, Filters

replace_letter_handler = MessageHandler(Filters.text & (~Filters.command), replace_letter)
dispatcher.add_handler(replace_letter_handler)
