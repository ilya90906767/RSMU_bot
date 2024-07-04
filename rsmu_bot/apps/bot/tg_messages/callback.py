from rsmu_bot.apps.bot.tg_messages.db_methods import get_primitive_message, get_is_auth, get_auth_user_info, get_unauth_user_info
from rsmu_bot.apps.bot.tg_messages.models import MainMessage,CurriculumsMessage
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import main_unauth,main_auth
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NavigationCallback


from aiogram import types
from aiogram import Router
from aiogram import F
from aiogram.types import Message

callback_router = Router()

@callback_router.callback_query(NavigationCallback.filter(F.cb_text.in_(["start", "auth_back"])))
async def start_callback(query: types.CallbackQuery):
    user_id = query.from_user.id 
    text = await get_primitive_message(MainMessage)
    user_is_auth = await get_is_auth(user_id)
    await query.message.delete(animation=True)
    if user_is_auth == False: 
        # await query.message.edit_text(text, reply_markup=main_unauth())
        await query.message.answer(text, reply_markup=main_unauth(),)
        await query.answer()
        
    if user_is_auth == True:
        # await query.message.edit_text(text, reply_markup=main_auth())
        await query.message.answer(text, reply_markup=main_auth())
        await query.answer()

@callback_router.callback_query(NavigationCallback.filter(F.cb_text.in_(["curriculums"])))
async def start_curriculums(query: types.CallbackQuery):
    text = await get_primitive_message(CurriculumsMessage)

    