from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callback_datas import lesson_callback


async def get_lesson_keyboard(lesson_id):
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
	    [
	        InlineKeyboardButton(
	        	text="Get lesson", 
	        	callback_data=lesson_callback.new(
	        		action="get_lesson",
	        		item_id=lesson_id
	        	)
	        ),
	    ], 
	])

	return keyboard


async def get_task_keyboard(task_id, lesson_id):
	keyboard = [
	        InlineKeyboardButton(
	        	text="Get task", 
	        	callback_data=lesson_callback.new(
	        		action="get_task",
	        		item_id=f'{task_id}__{lesson_id}'
	        	)
	        ),
	    ]

	return keyboard


async def get_test_keyboard(test_id, lesson_id):
	keyboard = [
	        InlineKeyboardButton(
	        	text="Get test", 
	        	callback_data=lesson_callback.new(
	        		action="get_test",
	        		item_id=f'{test_id}__{lesson_id}'
	        	)
	        ),
	    ]

	return keyboard


async def get_under_lesson_keyboard(lesson_id, test_id, task_id):
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
			await get_test_keyboard(test_id, lesson_id),
			await get_task_keyboard(task_id, lesson_id),
		])

	return keyboard