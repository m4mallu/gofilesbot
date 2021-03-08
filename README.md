# GoFilesBot 🗂

A simple Telegram Bot for Movie & file serving Groups (Can be say "Filter Bot")

## 💠 Mode of Operation:

- A Super group and channel need to perform the bot function.
- Members who send file names will search by the bot in channel and send the media to the member personally (As PM)
- Group members doesn't have access to the channel directly.
- Group will remain safe as the chat doesn't contain any media in it.
- If in an emergency, Authorized admins can delete entire group messages in ```/cleanchat``` command

## 💠 Requirements:
```
TG_BOT_TOKEN    - Obtained from @BotFather
APP_ID          - Obtained from my.telegram.org
API_HASH        - Obtained from my.telegram.org
TG_USER_SESSION - Run any userbot session maker(https://repl.it/@ayrahikari/pyrogram-session-maker)
CHANNELS        - List of Channel ids(Starts with -100) seperated by <space>
AUTH_USERS      - List of Autherized user ids separated by <space>
```
⚠️ **TG_USER_SESSION Must be  made from an admin User present in the Group & channels** ⚠️

## 💠 @BotFather Command:
```
/clanchat - Delete all the messages in Group
```

## 💠 Deploy:

### Easy Way:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/gofilesbot)

### Hard Way: 

Create **config.py** with variables as given below (Refer sample.config):

```
class Config(object):
    TG_BOT_TOKEN = "134448596:AAEIyo3EBVCN3qdd3TfrmQUxoI-eZVGvmI"
    APP_ID = int(123635)
    API_HASH = "1a417dd4fdf3ead2819ff35641daa16b"
    TG_USER_SESSION = "BQDGRUC0_qw2GVQ2gpLFaXOt0mrWg16cBZPATQvR8KThDzi-NRE1I9DB......"
    CHANNELS = [-10012233245, -100883635533]
    AUTH_USERS = [1134455567, 9244566948]

```
Run the following:

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## 💠 [LICENSE](https://choosealicense.com/licenses/gpl-3.0/)
- GPLv3

## 💠 Credits:

[DAN](https://t.me/haskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library

[SpEcHiDe](https://github.com/SpEcHiDe) for his [DeleteMessagesRoBot](https://github.com/SpEcHiDe/DeleteMessagesRoBot)

## 💠 Creator :

[Mallu Boy](https://t.me/m4mallu) In Telegram - [AS](https://t.me/space4renjith)