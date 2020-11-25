from aiogram import types
from asyncio import sleep as async_sleep

from loader import dp


@dp.message_handler()
async def bot_help(message: types.Message):
	await async_sleep(60)

	await message.delete()
