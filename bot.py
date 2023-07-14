import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import TOKEN

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button = InlineKeyboardMarkup(row_width=1)
button.insert(InlineKeyboardButton(
    text='Не сделано', callback_data='not_done'))

button_done = InlineKeyboardMarkup(row_width=1)
button_done.insert(InlineKeyboardButton(
    text='Выполнено', callback_data='done'))


@dp.callback_query_handler(text='not_done')
async def not_done(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=button_done)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
