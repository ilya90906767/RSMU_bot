import asyncio
from asgiref.sync import sync_to_async

from rsmu_bot.apps.bot.users.models import BotUser

@sync_to_async
def get_primitive_message(model):
    text = model.objects.get(state="A").message
    return text
@sync_to_async
def get_primitive_image(model):
    url = model.objects.get(state="A").image.path
    return url
@sync_to_async
def get_user_from_db(user_id):
    return BotUser.objects.get(user_id=user_id)

@sync_to_async
def get_unauth_user_info(user_id):
     user = BotUser.objects.get(user_id=user_id)
     first_name, second_name, third_name = user.first_name, user.second_name, user.third_name
     return first_name, second_name, third_name
 
@sync_to_async
def get_auth_user_info(user_id):
     user = BotUser.objects.get(user_id=user_id)
     first_name, second_name, third_name, course = user.first_name, user.second_name, user.third_name, user.course
     return first_name, second_name, third_name, course
 
@sync_to_async
def get_is_auth(user_id):
     user = BotUser.objects.get(user_id=user_id)
     is_auth = user.is_auth
     return is_auth