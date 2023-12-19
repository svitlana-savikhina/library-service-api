from datetime import date

from asgiref.sync import async_to_sync
from celery import shared_task

from borrowings.models import Borrow
from borrowings.telegram_utils import send_message
from library_service_api import settings


@shared_task
def send_borrowing_notification(text):
    async_to_sync(send_message)(
        bot_token=settings.TELEGRAM_BOT_TOKEN,
        chat_id=settings.TELEGRAM_CHAT_ID,
        text=text,
    )


@shared_task
def check_overdue_borrowings():
    today = date.today()
    overdue_borrowings = Borrow.objects.filter(
        expected_return_date__lte=today, actual_return_date__isnull=True
    )

    if overdue_borrowings:
        for borrowing in overdue_borrowings:
            send_borrowing_notification(str(borrowing))
    else:
        send_borrowing_notification("No borrowings overdue today!")
