from asgiref.sync import sync_to_async
from rsmu_bot.apps.bot.online_elder.models import ElderMessage, ElderMessageButtons, SubElderMessageButtons

from asgiref.sync import sync_to_async
from rsmu_bot.apps.bot.online_elder.models import ElderMessage, ElderMessageButtons, SubElderMessageButtons, SubSubElderMessageButtons

@sync_to_async
def get_online_elder_buttons(Modelname, id=None):
    if Modelname == "ElderMessage": 
        text = ElderMessage.objects.get(state="A").message
        buttons = list(ElderMessageButtons.objects.filter(state="A").values('id','title','message','image','link'))
        photo_url = ElderMessage.objects.get(state="A").image.path
        return text, buttons, photo_url
    elif Modelname ==  "ElderMessageButtons":
        elder_message_button = ElderMessageButtons.objects.get(state="A", id=id)
        text = elder_message_button.message
        sub_buttons = elder_message_button.get_sub_buttons()
        photo_url = elder_message_button.image.path
        link = elder_message_button.link
        if sub_buttons:
            buttons = list(sub_buttons.values('id','title','message','image','link'))
        else:
            buttons = []
        return text,buttons, photo_url, link
    elif Modelname == "SubElderMessageButtons":
        sub_elder_message_button = SubElderMessageButtons.objects.get(state="A", id=id)
        subsub_buttons = sub_elder_message_button.get_subsub_buttons()

        if subsub_buttons:
            buttons = list(subsub_buttons.values('id','title','message','image','link'))
        else:
            buttons = []

        print(sub_elder_message_button)
        text = sub_elder_message_button.message
        photo_url = sub_elder_message_button.image.path
        link = sub_elder_message_button.link
        print(link)
        return text,photo_url,link,buttons
    elif Modelname == "SubSubElderMessageButtons":
        subsub_elder_message_button = SubSubElderMessageButtons.objects.get(state="A", id=id)
        print(subsub_elder_message_button)
        text = subsub_elder_message_button.message
        photo_url = subsub_elder_message_button.image.path
        link = subsub_elder_message_button.link
        print(link)
        return text,photo_url,link