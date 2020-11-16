from json import loads 

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp, db 
from keyboards.inline.callback_datas import lesson_callback
from keyboards.inline.lesson_keyboards import *


@dp.callback_query_handler(lesson_callback.filter(action="get_test"))
async def send_test(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=0)

    items = list(map(int, callback_data['item_id'].split('__')))

    questions = await db.select_questions(items[0])

    await state.set_state("test")
    await state.update_data(
            lesson_id=items[1], 
            questions=[q['text'] for q in questions[1:]], 
            correct_answers=[q['answer'] for q in questions],
            current_answers=[]
        )

    question = questions[0]['text']

    keyboard = await get_under_test_keyboard(items[1])

    await call.message.edit_text(question, reply_markup=keyboard)


@dp.callback_query_handler(lesson_callback.filter(action="send_answer"), state='test')
async def update_test(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=0)

    data = await state.get_data()

    current_answers = data.get('current_answers')
    current_answers.append(callback_data['item_id'])

    await state.update_data(
            current_answers=current_answers
            )

    lesson_id = data.get('lesson_id')
    questions = data.get("questions")

    if questions:
        await state.update_data(questions=questions[1:])
        question = questions[0]

        keyboard = await get_under_test_keyboard(lesson_id)
        await call.message.edit_text(question, reply_markup=keyboard)

    else:
        data = await state.get_data()

        current_answers = data.get("current_answers")
        correct_answers = data.get("correct_answers")
        
        pairs = [i==j for i, j in zip(current_answers, correct_answers)]
        result = f'{pairs.count(True)} of {len(pairs)}'

        keyboard = await get_lesson_keyboard(lesson_id)
        await call.message.edit_text(result, reply_markup=keyboard)

        await state.finish()


@dp.callback_query_handler(lesson_callback.filter(action="back_to_lesson"), state='test')
async def send_lesson(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=0)

    await state.finish()

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
