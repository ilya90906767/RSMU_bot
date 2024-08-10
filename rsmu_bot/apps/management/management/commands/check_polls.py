from django.core.management.base import BaseCommand
from rsmu_bot.apps.bot.polls.db_checker import check_polls_main
import time
import logging
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
from aiogram import Bot

class Command(BaseCommand):
    help = "Check for bad polls"

    def handle(self, *args, **options):
        print('bad_polls started')
        while True:
            asyncio.run(check_polls_main())
            time.sleep(60)