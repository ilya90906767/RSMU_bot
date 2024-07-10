from rsmu_bot import settings
from rsmu_bot.apps.bot.tg_messages.db_methods import get_primitive_message, get_is_auth, get_auth_user_info, get_unauth_user_info, get_button_primitive_image
from rsmu_bot.apps.bot.tg_messages.db_methods import get_all_curriculums_buttons,get_all_subcurriculums_buttons,get_all_subsubcurriculums_buttons
from rsmu_bot.apps.bot.tg_messages.models import MainMessage,CurriculumsMessage,CurriculumsButtons,SubCurriculumsButtons,SubSubCurriculumsButtons
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import main_unauth,main_auth,curriculums,subcurriculums_buttons,subsubcurriculums_buttons,subsubsubcurriculums_buttons
from rsmu_bot.apps.bot.tg_keyboards.main_keyboards import NCM



from aiogram import types,Bot
from aiogram import Router
from aiogram import F
from aiogram.types import Message, InputFile, FSInputFile


callback_router = Router()

@callback_router.callback_query(NCM.filter(F.cb_text.in_(["start", "auth_back","curriculums_to_main"])))
async def start_callback(query: types.CallbackQuery):
    user_id = query.from_user.id 
    text = await get_primitive_message(MainMessage)
    user_is_auth = await get_is_auth(user_id)
    await query.message.delete(animation=True)
    if user_is_auth == False: 
        # await query.message.edit_text(text, reply_markup=main_unauth())
        await query.message.answer(text, reply_markup=main_unauth(query.message),)
        await query.answer()
        
    if user_is_auth == True:
        # await query.message.edit_text(text, reply_markup=main_auth())
        await query.message.answer(text, reply_markup=main_auth(query.message))
        await query.answer()

#Все кружки типо СНО и Спорт
@callback_router.callback_query(NCM.filter(F.cb_text.in_(["curriculums","from_subcurriculums_to_button","from_subsub_to_subcurriculums","from_subsubsub_to_subcurriculums"])))
async def start_curriculums(query: types.CallbackQuery,bot:Bot,callback_data: NCM):
    text = await get_primitive_message(CurriculumsMessage)
    all_curriculums_buttons = await get_all_curriculums_buttons(CurriculumsButtons)
    # print(all_curriculums_buttons)
    # print('Past meessge ID',callback_data.cb_message_id)
    await query.message.delete()
    await query.message.answer(text,reply_markup=curriculums(query.message,all_curriculums_buttons))
    
#Спортклуб -- выбираем киберклуб
@callback_router.callback_query(NCM.filter(F.cb_text.startswith("curriculums_button")))
async def start_curriculums(query:types.CallbackQuery,bot:Bot,callback_data: NCM):
    button_id = callback_data.cb_text.split("_")[2]
    all_curriculums_buttons = await get_all_curriculums_buttons(CurriculumsButtons)
    curriculum_button_title = next((item for item in all_curriculums_buttons if int(item["id"]) == int(button_id)))["title"]
    image_path = await get_button_primitive_image(CurriculumsButtons,curriculum_button_title)
    image_url = str(image_path)
    photo = FSInputFile(image_url)
    # print(image_url)
    curriculum_button_message = next((item for item in all_curriculums_buttons if int(item["id"]) == int(button_id)))["message"]
    all_sub_curriculums_buttons = await get_all_subcurriculums_buttons(SubCurriculumsButtons,int(button_id))
    # print(all_sub_curriculums_buttons)
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo, 
        caption=curriculum_button_message, 
        reply_markup=subcurriculums_buttons(int(button_id), all_sub_curriculums_buttons)
        )

#Киберклуб - выбираем доту
@callback_router.callback_query(NCM.filter(F.cb_text.startswith("subcurriculums_button_")))
async def start_subcurriculums(query: types.CallbackQuery, bot: Bot, callback_data: NCM):
    button_id = callback_data.cb_text.split("_")[2]
    all_subcurriculums_buttons = await get_all_subcurriculums_buttons(SubCurriculumsButtons, int(callback_data.cb_button_id))
    # print(all_subcurriculums_buttons)
    curriculum_button_title = next((item for item in all_subcurriculums_buttons if int(item["id"]) == int(button_id)))["title"]
    image_path = await get_button_primitive_image(SubCurriculumsButtons,curriculum_button_title)
    # print('IMAGE FOR CYBERCLUB', image_path)
    # print(all_subcurriculums_buttons)
    image_url = str(image_path)
    photo = FSInputFile(image_url)
    subcurriculums_button = next((item for item in all_subcurriculums_buttons if int(item["id"]) == int(button_id)))
    message_text = subcurriculums_button["message"]
    all_subsubcurriculums_buttons = await get_all_subsubcurriculums_buttons(SubSubCurriculumsButtons, int(button_id))
    print(all_subsubcurriculums_buttons)
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo, 
        caption=message_text, 
        reply_markup=subsubcurriculums_buttons(button_id, all_subsubcurriculums_buttons)
        )
    
@callback_router.callback_query(NCM.filter(F.cb_text.startswith("subsubcurriculums_button_")))
async def start_subsubcurriculums(query: types.CallbackQuery, bot: Bot, callback_data: NCM):
    button_id = callback_data.cb_text.split("_")[2]
    all_subsubcurriculums_buttons = await get_all_subsubcurriculums_buttons(SubSubCurriculumsButtons, int(callback_data.cb_message_id))
    curriculum_button_title = next((item for item in all_subsubcurriculums_buttons if int(item["id"]) == int(button_id)))["title"]
    print(curriculum_button_title)
    subsubcurriculums_button = next((item for item in all_subsubcurriculums_buttons if int(item["id"]) == int(button_id)))
    message_text = f"{subsubcurriculums_button['message']}\n"
    image_path = subsubcurriculums_button["image"]
    image_url = settings.MEDIA_ROOT + str(image_path) 
    print(image_url)
    photo = FSInputFile(image_url)
    link = subsubcurriculums_button.get('link', [])
    print(link)
    await query.message.delete()
    await query.message.answer_photo(
        photo=photo, 
        caption=message_text, 
        reply_markup=subsubsubcurriculums_buttons(button_id,link)
        )