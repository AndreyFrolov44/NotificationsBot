import os

from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

TOKEN = os.getenv('TOKEN')

TABLE_ID = os.getenv('TABLE_ID')
