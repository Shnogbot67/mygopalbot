import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Gopal Bhar Bot.
    
    
    
My Name: <a href='https://t.me/Gopalbharbot'>Gopal Bhar Bot</a>

Language : <a href='https://www.python.org'> Python V3</a>

Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

Server: <a href='Google.com'>Private</a>

Powered By: <a href='https://t.me/worldofmovies8'>WOM - BW Movies</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/royaldwip'>Private</a>
\n\nɪ Aᴍ Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Fɪɴᴅɪɴɢ Rᴏʙᴏᴛ.. 
Iғ Yᴏᴜ Dᴏɴ'ᴛ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ? 
Kᴏɪ Nᴀ Bᴀᴛᴀ Dᴇᴛʜᴀ Hᴏᴏɴ Mᴜᴊᴇ Kᴀɪsᴀ Usᴇ Kᴀʀᴇ! Wᴀsᴀ Yᴇ Mᴀᴛ Sᴀᴍᴊᴏ Mᴜᴊᴇ Eɴɢʟɪsʜ Nʜɪ Aᴛᴀ Hᴀɪɴ Mᴜᴊᴇ Aᴛᴀ Hᴀɪɴ Bᴜᴛ Bᴏʟᴛᴀ Nʜɪ Bᴇᴄᴀᴜsᴇ Eɴɢʟɪsʜ Iɴᴅɪᴀ Kᴀ Lᴀɴɢᴜᴀɢᴇ Nʜɪ HᴀɪN.. 
Bᴜᴛ Fʜɪʀ Bʜɪ Bᴏʟᴛᴀ Hᴏᴏɴ Kʏᴀ Kᴀʀᴇ Bᴀᴄʜᴘᴀɴ Sᴇ Sɪᴋʜɴᴀ Pᴀʀᴀ Nʜɪ Tᴏʜ Sɪʀ Eɴɢʟɪsʜ Pᴀʀ Mᴀʀᴋs Kᴀᴍ Kᴀʀ Dᴇᴛʜᴀ Hᴀɪɴ 🤣\n\nBᴇ Sᴇʀɪᴏᴜs Oᴋᴀʏ.. \n\nHᴀɴ Tᴏʜ Mᴜᴊᴇ Bᴀs Mᴏᴠɪᴇ Kᴀ Nᴀᴍ Lɪᴋʜᴇ Dᴏ Mᴇ Aᴘᴋɪ Jᴀʀᴏʀᴀᴛ Kɪ Mᴏᴠɪᴇ Kᴀ Lɪɴᴋ Dᴜɴɢᴀ Bᴜᴛ Cᴏɴᴅɪᴛɪᴏɴ Hᴀɪɴ Aᴘ Mᴜᴊᴇ Gᴀʟᴀᴛ Sᴘᴇʟʟɪɴɢ Nʜɪ Dᴇ Sᴀᴋᴛᴇ Nʜɪ Tᴏʜ Mᴇ Aᴘᴋᴏ Mᴏᴠɪᴇ Nʜɪ Dᴇ Pᴀʏᴏɴɢᴀ Oᴋᴀʏ.. \nFʜɪʀ Bʜɪ Aɢᴀʀ Sᴀᴍᴊ Nʜɪ Aᴛᴀ Hᴀɪɴ Mᴜᴊᴇ Usᴇ Kᴀɪsᴀ Kᴀʀᴇ Tᴏʜ Nɪᴄᴄʜᴇ Bᴜᴛᴛᴏɴ Pᴇ Cʟɪᴄᴋ  Kᴀʀᴋᴇ Dᴇᴋʜ Sᴀᴋᴛᴇ Hᴏᴏɴ. \n\nAᴜʀ Eᴋ Bᴀᴛ Aɢᴀʀ Mᴏᴠɪᴇ Mᴇʀᴇ Dᴀᴛᴀʙᴀsᴇ Pᴀʀ Nʜɪ Hᴀɪɴ Tᴏ Aᴘ Mᴇʀᴇ Oᴡɴᴇʀ Kᴏ Bᴏʟ Sᴀᴋᴛᴇ Hᴏᴏɴ Wᴏʜ Dᴀʟ Dᴇɢᴀ.. @Royaldwip\n\n🔴 Nᴏᴛᴇ :(\n(Pʜᴇʟᴇ Gᴏᴏɢʟᴇ Pᴇ Jᴀᴋᴇ Sᴘᴇʟʟɪɴɢ Cʜᴇᴋ Kᴀʀɴᴀ Fʜɪʀ Oᴡɴᴇʀ Kᴏ Bᴏʟɴᴀ Nʜɪ Tᴏ Bʟᴏᴄᴋ Bʜɪ Kᴀʀ Sᴀᴋᴛᴀ Hᴀɪɴ).</b>
"""

    HOME_TEXT = """
<b>Hey! {},

MY NAME IS GOPAL BHAR BOT

I CAN SEARCH MOVIES AND SERIES WHAT YOU WANT!\nIn Correct Spelling!!! 

<a>SEND MOVIE NAME WITH CORRECT SPELLING</a></b>
"""


    START_MSG = """
<b>Hey! {},

MY NAME IS GOPAL BHAR BOT

I CAN SEARCH MOVIES AND SERIES WHAT YOU WANT! 

<a>JOIN THIS BACKUP @WOMBACKUP</a></b>
"""

