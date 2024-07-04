#Importing packages
import asyncio
import logging
import os
from dotenv import load_dotenv

# from telebot.async_telebot import AsyncTeleBot
# from telebot.asyncio_handler_backends import ContinueHandling

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode 

#Importing handlers
from rsmu_bot.apps.bot.tg_messages.start import start_router
from rsmu_bot.apps.bot.tg_messages.callback import callback_router
from rsmu_bot.apps.bot.tg_messages.snils_auth import auth_router

#Importing models 
from rsmu_bot.apps.bot.tg_messages.models import *

load_dotenv()   
API_TOKEN=os.getenv('API_TOKEN')


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # Register all the routers from handlers package
    dp.include_routers(
        start_router,
        callback_router,
        auth_router
    )

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)
    

# @bot.message_handler(commands=['start']) #В идеале добавить inline, при нажатии которой выполнялся каллбек на изменение сообщения
# async def send_welcome(message):
#     text = await get_primitive_message(WelcomeMessage)
#     await bot.send_message(message.chat.id, text)
#     return ContinueHandling()

# @bot.message_handler(commands=['start'])
# async def send_main(message):
#     text = await get_primitive_message(MainMessage)
#     await bot.send_message(message.chat.id, text, reply_markup=main_unauth()) #надо сделать проверку на зарег юзера
#     return ContinueHandling()


# @bot.message_handler(commands=['register'])
# async def register(message):
#     text = await get_primitive_message(RegistrationMessage)
    
#     await bot.reply_to(message, text)
    

# @bot.message_handler(func=lambda message: True)
# async def unknown_message(message):
#     text = await get_primitive_message(UnknownMessage) 
#     await bot.reply_to(message, message.text)

