## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQATaXqbXHFHhi-BQTHANeEAaPryA5YvGpfDaWhhTQAV41DMScQBMrKhLHn_IgTKuI12T-geWqhe55-B3jDHYwAyBtRD3CbpnLhkR738G6i869TT9J2DU1kq_q1aNrjMPgERUrWJSEsQW0Emf4ZfiYaInpSG0qljBtiZrPKlGpArEO5gfnzEBk3ft_8P4yU_vwfw9ZQv6l9AafKwUuhKCGwJ04RaOepnz1ScgylZkA5lOcZlIOzvoSU2gMM-9o1NHpEfy2GFuiPMlOnn4VTN-YwtL-Dn2bV-GSIQB1yyT4WRn14Q7FLZxQzqZrnzDebdohBk6hoipvwUhlNV0P1O4gVaAAAAAS4fyOgA")
BOT_TOKEN = getenv("BOT_TOKEN", "2100234484:AAEb0S-CWC4h2Xr1rOUft9PvbqPKszSnCxQ")
BOT_NAME = getenv("BOT_NAME", "Shubhanshu")
API_ID = int(getenv("API_ID", "14486017"))
API_HASH = getenv("API_HASH", "e303f55d6a548e29ca7e91cadbd80182")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Florenza_xdd")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Starz_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "STARZ_BOTS")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
