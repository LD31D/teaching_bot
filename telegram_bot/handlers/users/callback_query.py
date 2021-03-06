from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, bot, db 
from keyboards.inline.callback_datas import lesson_callback
from keyboards.inline.lesson_keyboards import *


@dp.callback_query_handler(lesson_callback.filter(action="get_lesson"))
async def send_lesson(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=0)
    
    lesson_id = int(callback_data['first_value'])
    lesson = await db.select_lesson(lesson_id)

    if lesson['task_id'] and lesson['test_id']:
        keyboard = await get_under_lesson_keyboard(lesson['id'], lesson['test_id'], lesson['task_id'])
    else:
        keyboard = None

    if not call.message: 
        await bot.send_photo(
            call.from_user.id, 
            photo=lesson['image'], 
            caption=lesson['text'], 
            reply_markup=keyboard
            )

    else:
        await call.message.edit_caption(lesson['text'], reply_markup=keyboard)


@dp.callback_query_handler(lesson_callback.filter(action="get_task"))
async def send_task(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=0)

    task_id = int(callback_data['first_value'])
    lesson_id = int(callback_data['second_value'])

    task = await db.select_task(task_id)
    keyboard = await get_lesson_keyboard(lesson_id)

    await call.message.edit_caption(task['description'], reply_markup=keyboard)

