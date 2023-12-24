# Library Service Api
Online management system for book borrowings
## Features:
* JWT authenticated.
* Admin panel /admin/
* Documentation at /api/doc/swagger/
* Books borrowing management
* Notifications service through Telegram API
* Scheduled notifications with Celery and Redis

## Installation:
Python3 must be already installed

```shell
git clone https://github.com/svitlana-savikhina/library-service-api
cd library-service-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver #starts Django Server
```
Create .env file in root directory, define environment variables in it (example you can find in .env_sample)

## Run with Docker:
```shell
docker-compose build
docker-compose up
```

## Get Telegram notifications:
* Create bot using BotFather and get token as TELEGRAM_BOT_TOKEN
* Create a chat in Telegram to send notifications there and add a bot to this chat
* Using https://t.me/getmyid_bot find out the chat_id as TELEGRAM_CHAT_ID