from rsmu_bot.apps.bot.polls.models import PollsImage
import time 
from asgiref.sync import sync_to_async
import asyncio
from dotenv import load_dotenv
import os
from aiogram import Bot

@sync_to_async
def db_check():
    """Wrap the synchronous db_check function in an async context"""
    bad_polls = PollsImage.objects.filter(state="bad")
    if bad_polls.exists():
        return bad_polls
    else: 
        return None

@sync_to_async
def get_polls_user_ids(bad_polls):
    """Wrap the synchronous get_polls_user_ids function in an async context"""
    return [poll.user.user_id for poll in bad_polls]

@sync_to_async
def update_poll_state(poll):
    """Wrap the synchronous update_poll_state function in an async context"""
    poll.state = "bad_message_send"
    poll.save()

async def send_message(bad_polls, bot):
    user_ids = await get_polls_user_ids(bad_polls)
    for poll in bad_polls:
        await bot.send_message(chat_id=poll.user.user_id, text="Вы неправильно выполнили опрос")
        await update_poll_state(poll)  # Update the state of the poll to "uploaded"

async def check_polls_main():
    load_dotenv()   
    API_TOKEN=os.getenv('API_TOKEN')
    bot = Bot(token=API_TOKEN)
    polls = await db_check()  # Use await to call the async db_check function
    if polls is not None:
        await send_message(polls, bot)  # Use await to call the async send_message function

