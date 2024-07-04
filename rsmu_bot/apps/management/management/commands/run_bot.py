from django.core.management.base import BaseCommand, CommandError
from rsmu_bot.apps.bot.main_bot import main
import asyncio
import logging
import os
from dotenv import load_dotenv
load_dotenv()
    
class Command(BaseCommand):
    help = "Bot polling"
    
    def handle(self, *args, **options):
        print('Bot polling')
        logging.basicConfig(level=os.getenv("DJANGO_LOG_LEVEL", "INFO"))
        asyncio.run(main())
        