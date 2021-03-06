from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callback_datas import lesson_callback


async def get_lesson_keyboard(lesson_id):
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
	    [
	        InlineKeyboardButton(
	        	text="Get lesson", 
	        	callback_data=lesson_callback.new(
	        		action="get_lesson",
	        		first_value=lesson_id,
	        		second_value='None'
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
	        		first_value=task_id,
	        		second_value=lesson_id
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
	        		first_value=test_id,
	        		second_value=lesson_id
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


async def get_under_test_keyboard(lesson_id):
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
		[
			InlineKeyboardButton(
				text='A.',
				callback_data=lesson_callback.new(
					action='send_answer',
					first_value='a',
					second_value='None'
				)
			),
		],
		[
			InlineKeyboardButton(
				text='B.',
				callback_data=lesson_callback.new(
					action='send_answer',
					first_value='b',
					second_value='None'
				)
			),
		],
		[
			InlineKeyboardButton(
				text='C.',
				callback_data=lesson_callback.new(
					action='send_answer',
					first_value='c',
					second_value='None'
				)
			),
		],
	    [
	        InlineKeyboardButton(
	        	text="<<<", 
	        	callback_data=lesson_callback.new(
	        		action="back_to_lesson",
	        		first_value=lesson_id,
	        		second_value='None'
	        	)
	        ),
	    ], 
	])

	return keyboard