# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "10379650"))
API_HASH = getenv("API_HASH", "29813216c8daa138b7abbb3df3012c35")
BOT_TOKEN = getenv("BOT_TOKEN", "8249900669:AAHooErCq1W0pFW7EgkcFubIbaWRnl0NDJk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1182181055").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://vk5347775:cVy2Plb0ydaiIz3y@cluster0.oflmklz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002722363511")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001774379318"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
