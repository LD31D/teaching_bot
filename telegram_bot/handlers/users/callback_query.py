from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, bot, db 
from keyboards.inline.callback_datas import lesson_callback
from keyboards.inline.lesson_keyboards import *


@dp.callback_query_handler(lesson_callback.filter(action="get_lesson"))
async def send_lesson(call: CallbackQuery, callback_data: dict):
    lesson_id = int(callback_data['item_id'])
    lesson = await db.select_lesson(lesson_id)

    if lesson['task_id'] and lesson['test_id']:
        keyboard = await get_under_lesson_keyboard(lesson['id'], lesson['test_id'], lesson['task_id'])
    else:
        keyboard = None

    if not call.message: 
        await bot.send_message(call.from_user.id, lesson['text'], reply_markup=keyboard)

    else:
        await call.message.edit_text(lesson['text'], reply_markup=keyboard)


@dp.callback_query_handler(lesson_callback.filter(action="get_task"))
async def send_task(call: CallbackQuery, callback_data: dict):
    items = list(map(int, callback_data['item_id'].split('__')))

    task = await db.select_task(items[0])

    keyboard = await get_lesson_keyboard(items[1])

    await call.message.edit_text(task['description'], reply_markup=keyboard)


@dp.callback_query_handler(lesson_callback.filter(action="get_test"))
async def send_test(call: CallbackQuery, callback_data: dict):
    items = list(map(int, callback_data['item_id'].split('__')))

    questions = await db.select_questions(items[0])

    keyboard = await get_lesson_keyboard(items[1])

    await call.message.edit_text('description', reply_markup=keyboard)
