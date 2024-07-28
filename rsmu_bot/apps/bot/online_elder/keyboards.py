from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NCM

def ElderMessage_kb(buttons):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text="auth_back").pack())
    for button in buttons:
        builder.button(text=f"{button['title']}", callback_data=NCM(cb_button_id=button['id'], cb_text="ElderMessageButtons").pack())
    builder.adjust(1,2)
    return builder.as_markup()
def ElderMessageButtons_kb(buttons, link):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text="auth_back").pack())
    if buttons != []:
        for button in buttons:
            builder.button(text=f"{button['title']}", callback_data=NCM(cb_button_id=button['id'], cb_text="SubElderMessageButtons").pack())
    if link: 
        builder.button(text="Ссылка", url=link)
    builder.adjust(1,2)
    return builder.as_markup()
def SubElderMessageButtons_kb(link):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text="auth_back").pack())
    if link: 
        builder.button(text="Ссылка", url=link)
    builder.adjust(1,2)
    return builder.as_markup()