# ---------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------- #

import re
import os
import time

from bot import Bot
from presets import Presets
from base64 import b64decode
from hurry.filesize import size
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, StopPropagation

if os.environ.get("ENV", False):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.text)
async def bot_pm(client: Bot, message: Message):
    if message.text == "/start":
        await client.send_message(
            chat_id=message.chat.id,
            text=Presets.WELCOME_TEXT.format(message.from_user.first_name)
        )
        raise StopPropagation
    query_message = message.text.split(" ")[-1]
    query_bytes = query_message.encode("ascii")
    try:
        base64_bytes = b64decode(query_bytes)
        secret_query = base64_bytes.decode("ascii")
    except Exception:
        msg = await client.send_message(
            chat_id=message.chat.id,
            text=Presets.BOT_PM_TEXT,
            reply_to_message_id=message.message_id
        )
        time.sleep(6)
        try:
            await msg.delete()
            await message.delete()
        except Exception:
            pass
        return
    await client.send_message(
        chat_id=message.chat.id,
        text=Presets.WELCOME_TEXT.format(message.from_user.first_name)
    )
    if secret_query:
        for channel in Config.CHANNELS:
            async for messages in client.USER.search_messages(channel, secret_query, filter="document"):
                doc_file_names = messages.document.file_name
                file_size = size(messages.document.file_size)
                if re.search(rf'\b{secret_query}\b', doc_file_names, re.IGNORECASE):
                    media_name = messages.document.file_name.rsplit('.', 1)[0]
                    media_format = messages.document.file_name.split('.')[-1]
                    await client.send_chat_action(
                        chat_id=message.from_user.id,
                        action="upload_document"
                    )
                    try:
                        await client.copy_message(
                            chat_id=message.chat.id,
                            from_chat_id=messages.chat.id,
                            message_id=messages.message_id,
                            caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_DOC.format(media_name,
                                                                                        media_format, file_size)
                        )
                    except FloodWait as e:
                        time.sleep(e.x)
            async for messages in client.USER.search_messages(channel, secret_query, filter="video"):
                vid_file_names = messages.caption
                file_size = size(messages.video.file_size)
                if re.search(rf'\b{secret_query}\b', vid_file_names, re.IGNORECASE):
                    media_name = secret_query.upper()
                    await client.send_chat_action(
                        chat_id=message.from_user.id,
                        action="upload_video"
                    )
                    try:
                        await client.copy_message(
                            chat_id=message.chat.id,
                            from_chat_id=messages.chat.id,
                            message_id=messages.message_id,
                            caption=Config.GROUP_U_NAME+Presets.CAPTION_TEXT_VID.format(media_name, file_size)
                        )
                    except FloodWait as e:
                        time.sleep(e.x)
