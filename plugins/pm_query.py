# ---------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------- #

import re
import os
import time

from bot import Bot
from presets import Presets
from base64 import b64decode
from helper.file_size import get_size
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters

if os.environ.get("ENV", False):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.text)
async def bot_pm(client: Bot, message: Message):
    if message.text == "/start":
        await client.send_message(
            chat_id=message.chat.id,
            text=Presets.WELCOME_TEXT.format(message.from_user.first_name),
            parse_mode='html',
            disable_web_page_preview=True
        )
        return
    try:
        query_message = message.text.split(" ")[-1]
        query_bytes = query_message.encode("ascii")
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
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text=Presets.WELCOME_TEXT.format(message.from_user.first_name),
            parse_mode='html',
            disable_web_page_preview=True
        )
        if secret_query:
            for channel in Config.CHANNELS:
                # Looking for Document type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="document", limit=50):
                    doc_file_names = messages.document.file_name
                    file_size = get_size(messages.document.file_size)
                    if re.compile(rf'{doc_file_names}', re.IGNORECASE):
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
                # Looking for video type in messages
                async for messages in client.USER.search_messages(channel, secret_query, filter="video", limit=50):
                    vid_file_names = messages.caption
                    file_size = get_size(messages.video.file_size)
                    if re.compile(rf'{vid_file_names}', re.IGNORECASE):
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
    except Exception:
        return
