## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBEWk1Mek1Xynjpo1mBg0rZXD2uD5xbcPvlDv0-yKzwMLNoMH8ol4Y5LDrj8kPqg13nymyUORddEo92VfxTcM1ZqkDQECrGnjhR0fWve6DHXl565U-gneg3Yn-lWwMlpSMSDcTQz7wnZHquzsTm-5TC766yYNlvL6vQ6jrnoEr2mYr0wjMaE_mOEmZiJfhv4xLSSUsSMIKbamLfACqc0VW-p1hget-l9Opbo8pPlYAgTm7_ED3ldd6Wa2UeWlwo_1beja5vSGf8CPm-am4PUIkxwQ-d7iVKYD90g4fpZZilLavyqtf4rZSp3T8UmjEpR6I2bzbLpBKa0TprwjL-MTrDeJyNsQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5018072348:AAHmUzBQJfpYUhUbsNCYvKd5fevzYureQLw")
BOT_NAME = getenv("BOT_NAME", "Shubhanshu")
API_ID = int(getenv("API_ID", "14486017"))
API_HASH = getenv("API_HASH", "e303f55d6a548e29ca7e91cadbd80182")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DeCoDeSupport")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeCoDeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeCoDeSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
