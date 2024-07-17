import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from _main_ import conv
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_user_interaction(conv):

    # Send a message to the bot
    await conv.send_message("/start")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message is of type string
    assert isinstance(response.text, str)


""" @pytest.mark.anyio
async def test_user_interaction(conv):

    # Send a message to the bot
    await conv.send_message("hello")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message is of type string
    assert isinstance(response.text, str)

@pytest.mark.anyio
async def test_user_interaction(conv):

    # Send a message to the bot
    await conv.send_message("test a random text")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message is of type string
    assert isinstance(response.text, str)


 """

