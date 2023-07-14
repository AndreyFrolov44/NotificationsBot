import asyncio

from datetime import datetime
from celery import Celery
from google_table import GoogleTable
from bot import bot, button
from config import REDIS_HOST, REDIS_PORT, TABLE_ID


celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')

table = GoogleTable(
    'creds.json', TABLE_ID)


celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.get_notifications',
        'schedule': 10.0,
    },
}
celery.conf.timezone = 'UTC'


@celery.task
def send_message(tel_id: int, message: str):
    asyncio.run(bot.send_message(tel_id, message, reply_markup=button))


@celery.task
def get_notifications():
    notifications = table.get_notifications()
    for notification in notifications:
        datetime_format = '%d.%m.%Y %H:%M'
        end_time = datetime.strptime(
            f'{notification[2].value} {notification[3].value}', datetime_format)
        start_time = datetime.now()
        if end_time > start_time:
            send_message.apply_async(
                (int(notification[0].value), notification[1].value), eta=end_time)
