import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23647817"))
  API_HASH = os.environ.get("API_HASH", "fb26d17d9a64aaff4036b895d489ec3c")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6716757898:AAHCzvA0QCeHXoMG5MC9VPBsvSLK8BsgW0c")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "IllegalStoreRobot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001956168136"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "vipurl.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "c873cc2e2485e14f92428882cb47f025ff105cdf")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5281368582"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002010581020")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001956168136"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ɪʟʟᴇɢᴀʟ ᴅᴇᴠ](https://telegram.me/TheIllegalDev)

ɪ ᴀᴍ sᴜᴘᴇʀ ɴᴏᴏʙ!

[Donate Me](https://t.me/TheIllegalDev)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
