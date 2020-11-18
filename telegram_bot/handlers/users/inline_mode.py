from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart

from loader import dp, bot, db
from keyboards.inline.lesson_keyboards import get_lesson_keyboard


async def processing_lectures(lessons):
    if not lessons:
        result=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="No Lecture found",
                input_message_content=types.InputTextMessageContent(
                    message_text="Wait for lectures to be added"
                ),
                description="Wait for lectures to be added",
                thumb_url="https://bit.ly/3lbUCZy",
                ),
        ]

    else:
        result = []
        for lesson in lessons:
            result.append(
                    types.InlineQueryResultArticle(
                        id=lesson['id'],
                        title=lesson['name'],
                        input_message_content=types.InputTextMessageContent(
                            message_text=lesson['name'], 
                        ),
                        thumb_url=lesson['image'],
                        reply_markup=await get_lesson_keyboard(lesson['id'])
                    )
                )

    return result


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    lessons = await db.select_all_lessons()
    result = await processing_lectures(lessons)

    await query.answer(
        results=result,
        cache_time=5
    )


@dp.inline_handler()
async def query_with_text(query: types.InlineQuery):
    lessons = await db.select_all_lessons_like_name(query.query)
    result = await processing_lectures(lessons)

    await query.answer(
        results=result,
        cache_time=5
    )
