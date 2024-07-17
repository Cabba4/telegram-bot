import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

from dotenv import load_dotenv
load_dotenv()

# Your API ID and hash here
#you need to follow this page "https://blog.1a23.com/2020/03/06/how-to-write-integration-tests-for-a-telegram-bot/" to make this work
api_id = os.getenv('TEST_API_ID')
api_hash = os.getenv('TEST_API_HASH')
session_str = os.getenv('SESSION_STR')

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="session")
async def conv():
    client = TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
    await client.connect()
    async with client.conversation("https://t.me/JobTeaser_bot") as conv:
        yield conv


