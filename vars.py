

from os import environ

API_ID = int(environ.get("API_ID", "30827233"))
API_HASH = environ.get("API_HASH", "07f8d7e1c1f2cc3576503dd0ea183881")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "allhinditvserialsdaily")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/allhinditvserialsdaily")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7470773511"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")




