import telegram


from library_service_api import settings


async def send_message(
    bot_token=settings.TELEGRAM_BOT_TOKEN,
    chat_id=settings.TELEGRAM_CHAT_ID,
    text=None,
):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)
