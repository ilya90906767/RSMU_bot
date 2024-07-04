from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram import F
from aiogram.types import Message
from asgiref.sync import sync_to_async

from rsmu_bot.apps.bot.tg_messages.db_methods import get_primitive_message,get_user_from_db
from rsmu_bot.apps.bot.tg_messages.models import RegistrationMessage
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NavigationCallback
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import auth,main_unauth

from rsmu_bot.apps.bot.users.models import BotUser

auth_router = Router()

class Snils(StatesGroup):
    numbers = State()
    

@auth_router.callback_query(NavigationCallback.filter(F.cb_text == "auth"))
async def auth_callback(query: types.CallbackQuery, state: FSMContext):
    text = await get_primitive_message(RegistrationMessage)
    await state.set_state(Snils.numbers)
    await query.message.edit_text(text,reply_markup=auth())
    await state.update_data(message_id=query.message.message_id)

@auth_router.message(Snils.numbers)
async def process_snils(message: Message, state: FSMContext, bot:Bot):
    await state.update_data(snils=message.text)
    data = await state.get_data()
    snils_number = data['snils']
    past_message_id = int(data['message_id'])
    print(past_message_id)
    await bot.delete_message(message_id=past_message_id, chat_id=message.chat.id)
    user_id = message.from_user.id
    tg_user = await get_user_from_db(user_id)
    
    async_snils_authenticate = sync_to_async(tg_user.snils_authenticate)
    auth_result = await async_snils_authenticate(snils_number)
    if auth_result == "DoesNotExist": 
        await message.answer(f'Проверьте правильность введеного СНИЛС. Мы не нашли ваш СНИЛС в базе данных студентов',reply_markup=auth())
    if auth_result == "FormatError":
        await message.answer(f'Проверьте правильность введеного СНИЛС. Не соответствует формату',reply_markup=auth())
    if auth_result == "Success":
        await message.answer(f'Пользователь был авторизован.\nCнилс изменен на {snils_number}.',reply_markup=auth())

    
    
    
    
    

