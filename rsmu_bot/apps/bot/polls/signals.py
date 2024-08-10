# import os
# import nest_asyncio
# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from rsmu_bot.apps.bot.polls.models import PollsImage  # Ensure the model import is correct

# from aiogram import types
# from rsmu_bot.apps.bot.main_bot import Bot  # Import the Bot instance here
# from dotenv import load_dotenv
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode 

# load_dotenv()   
# API_TOKEN=os.getenv('API_TOKEN')
# bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# nest_asyncio.apply()

# import asyncio



# @receiver(pre_save, sender=PollsImage)
# def get_old_instance(sender, instance, **kwargs):
#     if instance.pk:  # If the instance is being updated
#         try:
#             old_instance = sender.objects.get(pk=instance.pk)
#             instance.old_state = old_instance.state
#         except sender.DoesNotExist:
#             instance.old_state = None

# @receiver(post_save, sender=PollsImage)
# def send_message_on_state_change(sender, instance, **kwargs):
#     if hasattr(instance, 'old_state') and instance.old_state is not None and instance.state != instance.old_state:
#         user = instance.user
#         if instance.state == 'bad':
#             message = f'Зачем обманывать университет?'

#         if instance.state == 'good':
#             message = f'Опрос 1 успешно обработан. Спасибо!'       
        
#         # Use asyncio to run the asynchronous send_message function
#         asyncio.run(send_async_message(user.user_id, message))

# async def send_async_message(chat_id, message):
#     await bot.send_message(chat_id=chat_id, text=message)
