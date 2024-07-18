from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NCM


class PCB(CallbackData, prefix="PollCallBack"):
    text: str = ""
    message_id: int = 0
    poll_id: int = 0

def start_polls_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=PCB(text="back").pack())
    builder.button(text="1",callback_data=PCB(poll_id=1, text="poll_id").pack())
    builder.button(text="2",callback_data=PCB(poll_id=2, text="poll_id").pack())
    builder.button(text="3",callback_data=PCB(poll_id=3, text="poll_id").pack())
    builder.adjust(1,3)
    return builder.as_markup()

def send_photo():
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=PCB(text="back").pack())
    builder.adjust(1)
    return builder.as_markup()

def success_uploaded():
    builder = InlineKeyboardBuilder()
    builder.button(text="На главную", callback_data=NCM(cb_text="success_uploaded_poll_to_main").pack())
    builder.adjust(1)
    return builder.as_markup()