#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # ID of Channels from which the bot should search files
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "").split())

    # Authorized users to perform delete messages in group
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

# ------------------------------------------ Optional Variables ------------------------------------------------------ #
    # Username of the group to tag in sending medias
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", "@MovieKeralam")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
