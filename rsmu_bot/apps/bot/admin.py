from django.contrib import admin

from rsmu_bot.apps.bot.tg_messages.models import * 
from rsmu_bot.apps.bot.users.models import StudentRaw, BotUser


# Register your models here.
admin.register(RegistrationMessage, WelcomeMessage, MainMessage, CurriculumsMessage, UnknownMessage)(admin.ModelAdmin)
admin.register(StudentRaw, BotUser)(admin.ModelAdmin)