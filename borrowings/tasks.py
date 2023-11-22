from celery import shared_task

from borrowings.telegram_utils import send_message
from library_service_api import settings


@shared_task
async def send_borrowing_notification(text):
    await send_message(
        bot_token=settings.TELEGRAM_BOT_TOKEN,
        chat_id=settings.TELEGRAM_CHAT_ID,
        text=text,
    )
