# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1234567
API_HASH = "ab1c23def45fg67890h123i45678j9kl"

# Get this from @Botfather
TOKEN = "1517305760:AAG53bV39zleWVGL85NBHLFfTPwqcjyAmn4"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://Jarvis:an1234mol@vcpb.eo0jr.mongodb.netvcpb?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1311769691,
    1024689872,
    1421068194
]

# The ID of the group where your bot streams
GROUP = -1001291663564

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
