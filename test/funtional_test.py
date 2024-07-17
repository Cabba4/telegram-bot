import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from _main_ import conv
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

