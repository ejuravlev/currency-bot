import os
import asyncio
from telegram import Bot
from api import CurrencyApi


token = os.environ.get('BOT_TOKEN')
chatid = os.environ.get('CHAT_ID')


async def main():
    bot = Bot(token=token)
    api = CurrencyApi()
    exchange = await api.get_currency('RUB', 'AMD')
    await bot.send_message(chat_id=chatid, text=f'🇦🇲 Курс драмма на сегодня: {exchange}')


if __name__ == '__main__':
    asyncio.run(main())
