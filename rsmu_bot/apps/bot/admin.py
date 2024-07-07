from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin

from rsmu_bot.apps.bot.tg_messages.models import * 
from rsmu_bot.apps.bot.users.models import StudentRaw, BotUser

class CurriculumsButtonsInline(NestedTabularInline):
    model=CurriculumsButtons

class CurriculumsMessageAdmin(NestedModelAdmin):
    inlines=[CurriculumsButtonsInline]
    

# Register your models here.
admin.register(RegistrationMessage, WelcomeMessage, MainMessage, UnknownMessage)(admin.ModelAdmin)
admin.register(StudentRaw, BotUser)(admin.ModelAdmin)
admin.site.register(CurriculumsMessage,CurriculumsMessageAdmin)