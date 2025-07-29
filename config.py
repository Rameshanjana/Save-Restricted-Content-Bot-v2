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

API_ID = int(getenv("API_ID", "28637708"))
API_HASH = getenv("API_HASH", "a4f3a1accecfe0663039e227d0429a1d")
BOT_TOKEN = getenv("BOT_TOKEN", "7388467230:AAGQwWgukjQsmx0VWMsnfA1FTE8hU6wBkes")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5346047673").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://vk5347775:cVy2Plb0ydaiIz3y@cluster0.oflmklz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002838329809")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002883358480"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
