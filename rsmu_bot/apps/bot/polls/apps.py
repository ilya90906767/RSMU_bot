from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rsmu_bot.apps.bot.polls'

    def ready(self):
        import rsmu_bot.apps.bot.polls.signals # import the signals module
