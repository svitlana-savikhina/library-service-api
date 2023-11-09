from asgiref.sync import async_to_sync
from celery import shared_task


from borrowings.telegram_utils import send_message


@shared_task
def send_borrowing_notification(text):
    async_to_sync(send_message)(text=text)
