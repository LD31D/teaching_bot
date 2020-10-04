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
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
	    [
	        InlineKeyboardButton(
	        	text="Get lesson", 
	        	callback_data=lesson_callback.new(
	        		action="get_task",
	        		item_id=f'{task_id}__{lesson_id}'
	        	)
	        ),
	    ], 
	])

	return keyboard

