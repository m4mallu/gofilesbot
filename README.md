# GoFilesBot 🗂

A Telegram Filter bot (Especially for movie groups) differed with its mode of operation.

## 💠 Mode of Operation:

- A Super group and channel need to perform the bot function.
- Members who send file names will search by the bot in channel and send the media to the member personally (as PM)
- Group members doesn't have access to the channel directly.
- Group will remain safe as the chat doesn't contain any media in it.
- If in an emergency, Authorized admins can delete entire group messages in ```/cleanchat``` command

### Advantage :
1. Users don't have access to the main channel will help to avoid copyright infringement
2. Medias will only get from bot as pm only when asked in the Movie group.
3. Absence of media in the group will help to avoid copyright infringement.
3. Medias won't get from bot in direct PM (Except a vulnerability - Pros can find it.., lads keep playing..)
4. Finally, filter objects doesn't need to be added in the bot as the bot is searching in realtime with the key-word.

## 💠 Requirements:
```
TG_BOT_TOKEN    - Get from @BotFather
APP_ID          - Get from my.telegram.org
API_HASH        - Get from my.telegram.org
TG_USER_SESSION - Run any userbot session maker(https://repl.it/@ayrahikari/pyrogram-session-maker)
CHANNELS        - List of Channel ids (Starts with -100) seperated by <space>
AUTH_USERS      - List of Autherized user ids separated by <space>
GROUP_U_NAME    - Username of the group to tag in sending medias
```
⚠️ **TG_USER_SESSION Must be  made from an admin User present in the Group & channels** ⚠️

## 💠 @BotFather Command:
```
/cleanchat - Delete all the messages in Group (Only done by AUTH USERS)
```

## 💠 Deploy:

### Setup:

- Create a bot using @BotFather.
- Add the bot to Supergroup where bot need to do the function. 
- After adding the bot to Group, disable 'Groups' in @BotFather (Else, Someone will do the same in another Group 😂)
- Get APP ID and API HASH from my.telegram.org.
- Add the bot to channels and Group as necessary admin rights.
- Create a string session file with admin user exists in all the channels & Group.
- Deploy the bot in Heroku / VPS 
- Send a message in channels where bot need to fetch. (Can delete the message after.)
- It's all done. See the magic in Groups 😍


### Deploy Easy Way:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/gofilesbot)

### Deploy Hard Way: 

Create **config.py** with variables as given below (Refer sample.config):

```
class Config(object):
    TG_BOT_TOKEN = "134448596:AAEIyo3EBVCN3qdd3TfrmQUxoI-eZVGvmI"
    APP_ID = int(123635)
    API_HASH = "1a417dd4fdf3ead2819ff35641daa16b"
    TG_USER_SESSION = "BQDGRUC0_qw2GVQ2gpLFaXOt0mrWg16cBZPATQvR8KThDzi-NRE1I9DB......"
    CHANNELS = [-10012233245, -100883635533]
    AUTH_USERS = [1134455567, 9244566948]
    
# ------------- Optional ------------- #
    GROUP_U_NAME = "@my_group_name"

```
Run the following:

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## 💠 LICENSE

- [GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## 💠 Credits:

[DAN](https://t.me/haskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library

[SpEcHiDe](https://github.com/SpEcHiDe) for his [DeleteMessagesRoBot](https://github.com/SpEcHiDe/DeleteMessagesRoBot)

## 💠 Creator :

[Mallu Boy](https://t.me/m4mallu) In Telegram - [AS](https://t.me/space4renjith)
