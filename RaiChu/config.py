## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBZo31VJxwkIj-xp6F532h7W8eu9eMevTgPBl0p5Yay1K5GkNX8pddI9Ce0u5JdYqXerR5wMNsPSh0Q5efUnY6AdUih1CqvaJB0XP1sASTVy89KhH2D8ZqODxIjHvE7FlVU9GI93IEFIdB_hLRc7lMay2aSZRAfGMlk0UPetQaUWIb2E5jBiUNCGkb5tblDPKtCyuqWgnYnP2zBajHlT6ex30nt1fZVia5x4wuZVc8ZFvG1FSQAzgbJDJ9tMpTfAwgxMsX514T2uQxFX0TeBHXKOh0ytPJx2MIA4oYZK8VQ5VOzm6VKszWmIVM3c8KJRmWYf3Ofrio7e2iFjTiCzUIkAAAAATcKBl0A")
BOT_TOKEN = getenv("BOT_TOKEN", "5087891585:AAFT2Cis64pGMv5TXIHLrHjzcUoEQAbfsL4")
BOT_NAME = getenv("BOT_NAME", "VEXERA")
API_ID = int(getenv("API_ID", "12281520"))
API_HASH = getenv("API_HASH", "60fb92420c4797fb1e1af54a16edaf55")
OWNER_NAME = getenv("OWNER_NAME", "ABHISHEK_XDD")
ALIVE_NAME = getenv("ALIVE_NAME", "VEXERAMUSICS")
BOT_USERNAME = getenv("BOT_USERNAME", "VEXERA_ROBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VEXERA_MUSICS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SNEHABHI_SERVER")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "VEXERA_UPDATES")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5079644547").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
