""" import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import pytest_asyncio
from dotenv import load_dotenv
load_dotenv()
# Your API ID and hash here
api_id = os.getenv('TEST_API_ID')
api_hash = os.getenv('TEST_API_HASH')
session_str = os.getenv('SESSION_STR')



with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save()) """