from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class NavigationCallback(CallbackData, prefix="NavCallback"):
    cb_text: str

def start():
    builder = InlineKeyboardBuilder()
    builder.button(text="Начать", callback_data=NavigationCallback(cb_text="start").pack())
    builder.adjust(1)
    return builder.as_markup()
    
def main_unauth():
    builder = InlineKeyboardBuilder()
    builder.button(text="Авторизоваться", callback_data=NavigationCallback(cb_text="auth").pack())
    builder.button(text="Внеучебная деятельность", callback_data=NavigationCallback(cb_text="curriculums").pack())
    builder.button(text="Онлайн староста", callback_data=NavigationCallback(cb_text="online_elder").pack())
    builder.adjust(1,2)

    return builder.as_markup()

def main_auth():
    builder = InlineKeyboardBuilder()
    builder.button(text="Внеучебная деятельность", callback_data=NavigationCallback(cb_text="curriculums").pack())
    builder.button(text="Онлайн староста", callback_data=NavigationCallback(cb_text="online_elder").pack())
    builder.button(text="Связь с руководством", callback_data=NavigationCallback(cb_text="feedback").pack())
    builder.button(text="Личный кабинет", callback_data=NavigationCallback(cb_text="account").pack())
    builder.button(text="Навигация", callback_data=NavigationCallback(cb_text="navigation").pack())
    builder.adjust(2)
    return builder.as_markup()
    
    
    
def auth():
    backButton = InlineKeyboardButton(text="Назад", callback_data=NavigationCallback(cb_text="auth_back").pack())
    keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
        [backButton]
    ])
    return keyboard_inline

