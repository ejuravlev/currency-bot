import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from api import CurrencyApi


token = os.environ.get('BOT_TOKEN')
chatid = os.environ.get('CHAT_ID')

logging.basicConfig(
    format='[APP]: %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def get_currency_exchange():
    api = CurrencyApi()
    exchange = await api.get_currency('RUB', 'AMD')
    if exchange:
        return exchange
    else:
        return 'Что-то пошло не так при запросе к апи'


async def start_bot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    exchange_result = await get_currency_exchange()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'🇦🇲 Курс драмма на сегодня: {exchange_result}'
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler('start', start_bot_command)
    application.add_handler(start_handler)
    application.run_polling()
