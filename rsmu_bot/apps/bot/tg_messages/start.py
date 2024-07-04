from rsmu_bot.apps.bot.tg_messages.db_methods import get_primitive_message, get_user_from_db, get_primitive_image
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import start
from rsmu_bot.apps.bot.tg_messages.models import WelcomeMessage
from rsmu_bot.apps.bot.users.models import BotUser





from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    current_user_id = message.from_user.id
    try: 
        user = await get_user_from_db(current_user_id)
        text = await get_primitive_message(WelcomeMessage)
        image_path = await get_primitive_image(WelcomeMessage)
        photo = FSInputFile(image_path)
        await message.answer_photo(
            caption = f"{text}", 
            photo=photo,
            reply_markup=start(),
            show_caption_above_media=True
            )
    except ObjectDoesNotExist:
        user = BotUser(user_id=current_user_id, first_name=message.from_user.first_name)
        await sync_to_async(user.save)()
        text = await get_primitive_message(WelcomeMessage)
        image_path = await get_primitive_image(WelcomeMessage)
        photo = FSInputFile(image_path)
        await message.answer_photo(
            caption = f"{text}", 
            photo=photo,
            reply_markup=start(),
            show_caption_above_media=True
            )
        

