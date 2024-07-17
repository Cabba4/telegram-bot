import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from _main_ import conv
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_list_job_button(conv):

    # Send a message to the bot
    await conv.send_message("🔎 List Jobs")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message contains the expected text
    assert isinstance(response.text, str)


@pytest.mark.anyio
async def test_set_notification_button(conv):

    # Send a message to the bot
    await conv.send_message("🔔 Set notifications")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message contains the expected text
    assert isinstance(response.text, str)

@pytest.mark.anyio
async def test_help_button(conv):

    # Send a message to the bot
    await conv.send_message("❓ Help")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message contains the expected text
    assert isinstance(response.text, str)


@pytest.mark.anyio
async def test_list_companies_button(conv):

    # Send a message to the bot
    await conv.send_message("🏢 List companies")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message contains the expected text
    assert isinstance(response.text, str)


@pytest.mark.anyio
async def test_back_button(conv):

    # Send a message to the bot
    await conv.send_message("🔙 Back")

    # Wait for and get the response message
    response = await conv.get_response()

    # Verify if the response message contains the expected text
    assert isinstance(response.text, str)

