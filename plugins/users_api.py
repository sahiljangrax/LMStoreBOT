# © Telegram : @LMOwnerBot , GitHub : @VJBots

# Don't Remove Credit Tg - @LMOwnerBot
# Subscribe YouTube Channel For Amazing Bot https://www.youtube.com/@nokplayz7031
# Ask Doubt on telegram @LMOwnerBot

import requests
import json
from motor.motor_asyncio import AsyncIOMotorClient
from plugins.clone import mongo_db

# Don't Remove Credit Tg - @LMOwnerBot
# Subscribe YouTube Channel For Amazing Bot https://www.youtube.com/@nokplayz7031
# Ask Doubt on telegram @LMOwnerBot

async def get_short_link(user, link):
    api_key = user["shortener_api"]
    base_site = user["base_site"]
    print(user)
    response = requests.get(f"https://{base_site}/api?api={api_key}&url={link}")
    data = response.json()
    if data["status"] == "success" or rget.status_code == 200:
        return data["shortenedUrl"]

# Don't Remove Credit Tg - @LMOwnerBot
# Subscribe YouTube Channel For Amazing Bot https://www.youtube.com/@nokplayz7031
# Ask Doubt on telegram @LMOwnerBot

async def get_user(user_id):
    user_id = int(user_id)
    user = mongo_db.user.find_one({"user_id": user_id})
    if not user:
        res = {
            "user_id": user_id,
            "shortener_api": None,
            "base_site": None,
        }
        mongo_db.user.insert_one(res)
        user = mongo_db.user.find_one({"user_id": user_id})
    return user

# Don't Remove Credit Tg - @LMOwnerBot
# Subscribe YouTube Channel For Amazing Bot https://www.youtube.com/@nokplayz7031
# Ask Doubt on telegram @LMOwnerBot

async def update_user_info(user_id, value:dict):
    user_id = int(user_id)
    myquery = {"user_id": user_id}
    newvalues = { "$set": value }
    mongo_db.user.update_one(myquery, newvalues)

# Don't Remove Credit Tg - @LMOwnerBot
# Subscribe YouTube Channel For Amazing Bot https://www.youtube.com/@nokplayz7031
# Ask Doubt on telegram @LMOwnerBot
