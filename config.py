from os import getenv, path

from dotenv import load_dotenv

# Load variables from .env
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Twitch Config
TWITCH_ACCESS_TOKEN = getenv("ACCESS_TOKEN")
TWITCH_REFRESH_TOKEN = getenv("TWITCH_REFRESH_TOKEN")
TWITCH_CLIENT_ID = getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = getenv("TWITCH_CLIENT_SECRET")
TWITCH_CALLBACK_ROUTE = getenv("TWITCH_CALLBACK_ROUTE")
TWITCH_CHANNELS = getenv("TWITCH_CHANNELS")
