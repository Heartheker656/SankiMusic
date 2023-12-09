import os
import re
import sys

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Shalu music")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5336023580").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "5c9a06f4-40e5-4fff-b8ae-3ffaa67e1352")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "shalinisankimusicbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Shalini77986/shalinimusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ShaliniMusicBotSh")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/music_world_sh")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "54000"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "7f92897a59464ddbbf00f06cd6bda7fc")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2a230af10e0a40638dc77c1febb47170")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "sankilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/c32474d2e1f3b49854086.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/48a84e0bf6223ce724632.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph/file/22705f451bebc91c6e070.jpg"
GLOBAL_IMG_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
STATS_IMG_URL = "https://telegra.ph/file/4a6d9f4f3c3af2870451e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/a28dbc0fd7934a0bcb85e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "SankiMusic/resource/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/48a84e0bf6223ce724632.jpg"

if START_IMG_URL:
    if START_IMG_URL != "SankiMusic/resource/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/c32474d2e1f3b49854086.jpg"
