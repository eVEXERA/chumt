## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA_4viwXwUzirItFK3Op40QZGgstJ7ybzswBpscvkYRXAjQilqw19SbHn38Y7_5en2fmhv5zDYjLNPmfpwNIkIfgLlP0hnSwkew8SmGXBfQ5POli6PW3L9B-zAkGImxmeDvx6s8TpMMiu0INT7E2tCSA1SLBo3vllhTvPjQH9A-w8WqC6QLjGHSkdLTLJKv0vXBZk1-JL26xOXDbulPcr4oT2bzOCmeI99DFb-_fMKXJREdP05alkwW7uodE5uB5ePLd54CqREmKljD1MUS2jm0QI8ffseUxHiiL9qklhrclOcp0-xaOO71h_k1yfcPD_Bso22xLHLhzTDeG8TxcU2FfQ9-TwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1678144605:AAGe6pV3sxyc5dyJhjA0AQ_f3USanFfYkGY")
BOT_NAME = getenv("BOT_NAME", "Shubhanshu")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shadow_Helper_1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
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
