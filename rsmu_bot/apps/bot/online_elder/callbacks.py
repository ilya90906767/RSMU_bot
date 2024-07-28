from aiogram import Router, F, types
from aiogram.types import FSInputFile

from rsmu_bot.apps.bot.online_elder.db_methods import get_online_elder_buttons
from rsmu_bot.apps.bot.online_elder.models import ElderMessage, ElderMessageButtons
from rsmu_bot.apps.bot.tg_messages.db_methods import get_primitive_message
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NCM
from rsmu_bot.apps.bot.online_elder.keyboards import ElderMessage_kb, ElderMessageButtons_kb,SubElderMessageButtons_kb
online_elder_callback = Router()

@online_elder_callback.callback_query(NCM.filter(F.cb_text.in_(["online_elder"])))
async def start_online_elder(query: types.CallbackQuery, callback_data: NCM):
    text, buttons, photo_url = await get_online_elder_buttons(Modelname="ElderMessage")
    print(str(photo_url))
    photo = FSInputFile(str(photo_url))
    print(photo)
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=ElderMessage_kb(buttons)
    )
@online_elder_callback.callback_query(NCM.filter(F.cb_text.in_(["ElderMessageButtons"])))
async def start_elder_buttons(query: types.CallbackQuery, callback_data: NCM):
    elder_message_button_id = callback_data.cb_button_id
    text, buttons, photo_url, link = await get_online_elder_buttons(Modelname="ElderMessageButtons", id=elder_message_button_id)
    photo = FSInputFile(str(photo_url))
    print(text, buttons, photo_url)
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=ElderMessageButtons_kb(buttons, link)
    )

@online_elder_callback.callback_query(NCM.filter(F.cb_text.in_(["SubElderMessageButtons"])))
async def start_subelder_buttons(query: types.CallbackQuery, callback_data: NCM):
    subelder_message_button_id = callback_data.cb_button_id
    text, photo_url, link = await get_online_elder_buttons(Modelname="SubElderMessageButtons", id=subelder_message_button_id)
    photo = FSInputFile(str(photo_url))
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=SubElderMessageButtons_kb(link)
    )