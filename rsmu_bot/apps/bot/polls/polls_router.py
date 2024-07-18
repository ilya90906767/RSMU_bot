import os
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram import types,F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from rsmu_bot import settings
from rsmu_bot.apps.bot.main_bot import Bot
from rsmu_bot.apps.bot.polls.models import PollsImage
from rsmu_bot.apps.bot.polls.polls_keyboard import PCB, success_uploaded
from rsmu_bot.apps.bot.polls.polls_keyboard import start_polls_keyboard, send_photo
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NCM
from rsmu_bot.apps.bot.tg_messages.db_methods import get_user_id_from_tg_user_id, upload_poll_photo_by_user_id

from django.core.files.uploadedfile import SimpleUploadedFile


class PhotoState(StatesGroup):
    waiting_for_photo = State()
    poll_id = State()

polls_router = Router()

@polls_router.callback_query(NCM.filter(F.cb_text.in_(["start_polls"])))
async def start_polls(query: types.CallbackQuery):
    text = "Привет Волонтер! Выбери опросник"
    await query.message.delete(animation=True)
    await query.message.answer(text, reply_markup=start_polls_keyboard())
    await query.answer()

@polls_router.callback_query(PCB.filter(F.text.in_(["poll_id"])))
async def start_polls(query: types.CallbackQuery, bot: Bot, callback_data:PCB, state: FSMContext):
    await query.message.delete(animation=True)
    poll_id = callback_data.poll_id
    await state.set_state(PhotoState.waiting_for_photo)
    await state.update_data(poll_id=poll_id)
    text = "Теперь отправь скрин о том, что ты прошел опрос"
    await query.message.answer(text, reply_markup=send_photo())
    await query.answer()
    await state.update_data(message_id=query.message.message_id)

@polls_router.message(PhotoState.waiting_for_photo)
async def process_photo(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    file_info = await bot.get_file(photo_file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    data = await state.get_data()

    user_tg_id = message.from_user.id
    user = await get_user_id_from_tg_user_id(user_tg_id)

    media_root = settings.MEDIA_ROOT
    file_name = f'temp_{photo_file_id}.jpg'
    file_path = os.path.join(media_root, 'polls_images', file_name)  # add 'polls_images' directory

    with open(file_path, 'wb') as f:
        f.write(downloaded_file.getbuffer())

    # Create a Django file object from the temporary file
    with open(file_path, 'rb') as f:
        file_obj = SimpleUploadedFile(file_name, f.read(), content_type='image/jpeg')

    # Create a new PollsImage instance and save it to the database
    upload_result = await upload_poll_photo_by_user_id(user,file_obj,data)

    os.remove(file_path)

    if upload_result == True:  # check if the image was saved successfully
        text = "Мы загрузили ваше фото опросника. Ожидайте, его проверят в скором времени"
        await message.answer(text, reply_markup=success_uploaded())