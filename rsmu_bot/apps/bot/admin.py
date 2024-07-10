from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline

from rsmu_bot.apps.bot.tg_messages.models import * 
from rsmu_bot.apps.bot.users.models import StudentRaw, BotUser

class SubSubCurriculumsButtons(NestedStackedInline):
    model=SubSubCurriculumsButtons
    extra = 0

class SubCurriculumsButtonsInline(NestedStackedInline):
    model=SubCurriculumsButtons
    inlines=[SubSubCurriculumsButtons]
    extra = 0

class CurriculumsButtonsInline(NestedStackedInline):
    model=CurriculumsButtons
    inlines=[SubCurriculumsButtonsInline]
    extra = 0

class CurriculumsMessageAdmin(NestedModelAdmin):
    inlines=[CurriculumsButtonsInline]
    extra = 0

# Register your models here.
admin.site.register(RegistrationMessage, admin.ModelAdmin)
admin.site.register(WelcomeMessage, admin.ModelAdmin)
admin.site.register(MainMessage, admin.ModelAdmin)
admin.site.register(UnknownMessage, admin.ModelAdmin)
admin.site.register(StudentRaw, admin.ModelAdmin)
admin.site.register(BotUser, admin.ModelAdmin)
admin.site.register(CurriculumsMessage, CurriculumsMessageAdmin)