import asyncio
from asgiref.sync import sync_to_async

from rsmu_bot.apps.bot.polls.models import PollsImage
from rsmu_bot.apps.bot.users.models import BotUser

@sync_to_async
def get_user_id_from_tg_user_id(user_id):
     bot_user = BotUser.objects.get(user_id=user_id)
     return bot_user

@sync_to_async
def upload_poll_photo_by_user_id(user, image, data):
    polls_image = PollsImage(
        user=user,
        image=image,
        poll_number=data['poll_id'],
    )
    
    polls_image.save()
    return True

@sync_to_async
def get_primitive_message(model):
    text = model.objects.get(state="A").message
    return text
@sync_to_async
def get_primitive_image(model):
    url = model.objects.get(state="A").image.path
    return url

@sync_to_async
def get_button_primitive_image(model,title):
    url = model.objects.get(state="A",title=title).image.path
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

@sync_to_async
def get_all_curriculums_buttons(model): 
     curriculums_buttons=list(model.objects.filter(state="A").values('id','title','message','image'))
     return curriculums_buttons

@sync_to_async
def get_all_subcurriculums_buttons(model,curriculums_buttons_id): 
     sub_curriculums_buttons=list(model.objects.filter(state="A",curriculums_buttons=curriculums_buttons_id).values('id','title','message','image','link','curriculums_buttons'))
     return sub_curriculums_buttons

@sync_to_async
def get_all_subsubcurriculums_buttons(model, subcurriculums_button_id): 
     subsub_curriculums_buttons=list(model.objects.filter(state="A", subcurriculums_buttons_id=subcurriculums_button_id).values('id','title','message','image','link'))
     return subsub_curriculums_buttons

