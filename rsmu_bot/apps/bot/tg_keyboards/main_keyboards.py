from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class NCM(CallbackData, prefix="NavCallbackWithMessageID"): #NCM - navigation callback with message id
    cb_text: str
    cb_message_id: int = 0
    cb_button_id: int = 0

def start(message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Начать", callback_data=NCM(cb_text="start",cb_message_id=message.message_id).pack())
    builder.adjust(1)
    return builder.as_markup()
    
def main_unauth(message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Авторизоваться", callback_data=NCM(cb_text="auth",cb_message_id=message.message_id).pack())
    builder.button(text="Внеучебная деятельность", callback_data=NCM(cb_text="curriculums",cb_message_id=message.message_id).pack())
    builder.button(text="Онлайн староста", callback_data=NCM(cb_text="online_elder",cb_message_id=message.message_id).pack())
    builder.adjust(1,2)

    return builder.as_markup()

def main_auth(message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Внеучебная деятельность", callback_data=NCM(cb_text="curriculums",cb_message_id=message.message_id).pack())
    builder.button(text="Онлайн староста", callback_data=NCM(cb_text="online_elder",cb_message_id=message.message_id).pack())
    builder.button(text="Связь с руководством", callback_data=NCM(cb_text="feedback",cb_message_id=message.message_id).pack())
    builder.button(text="Личный кабинет", callback_data=NCM(cb_text="account",cb_message_id=message.message_id).pack())
    builder.button(text="Навигация", callback_data=NCM(cb_text="navigation",cb_message_id=message.message_id).pack())
    builder.adjust(2)
    return builder.as_markup()
    
def auth():
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text="auth_back").pack())
    builder.adjust(2)
    return builder.as_markup()

def curriculums(message, all_curriculums_buttons):
    builder = InlineKeyboardBuilder()
    builder.button(text="На главную", callback_data=NCM(cb_text=f"curriculums_to_main",cb_message_id=message.message_id).pack())

    for button in all_curriculums_buttons:
        builder.button(text=f"{button['title']}",callback_data=NCM(cb_text=f"curriculums_button_{button['id']}",cb_message_id=message.message_id).pack())
    builder.adjust(1,3)
    return builder.as_markup()

def subcurriculums_buttons(button_id,all_sub_curriculums_buttons):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text=f"from_subcurriculums_to_button",cb_button_id=button_id).pack())
    for button in all_sub_curriculums_buttons:
        builder.button(text=f"{button['title']}",callback_data=NCM(cb_text=f"subcurriculums_button_{button['id']}",cb_button_id=button_id).pack())
    builder.adjust(1,3)
    return builder.as_markup()

def subsubcurriculums_buttons(button_id, all_subsubcurriculums_buttons):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text=f"from_subsub_to_subcurriculums", cb_message_id=button_id).pack())
    for button in all_subsubcurriculums_buttons:
        builder.button(text=f"{button['title']}", callback_data=NCM(cb_text=f"subsubcurriculums_button_{button['id']}", cb_message_id=button_id).pack())
    builder.adjust(1, 3)
    return builder.as_markup()

def subsubsubcurriculums_buttons(button_id, link):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=NCM(cb_text=f"from_subsubsub_to_subcurriculums", cb_message_id=button_id).pack())
    if link:
        builder.button(text="Ссылка", url=link)
    
    builder.adjust(1)
    return builder.as_markup()
    

    
