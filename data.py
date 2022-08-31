from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/crossouy")],
        [
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="help"), 
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/itsdaps")],
    ]

    START = """
**Hey** {}

**Welcome to** {} 

**Jika Kamu Tidak Percaya Bot Ini** ? 
1. ɢᴀᴜsᴀʜ ʙᴀᴄᴀ ᴘᴇsᴀɴ ɪɴɪ
2. ʙʟᴏᴋɪʀ ʙᴏᴛ ᴀᴛᴀᴜ ᴅᴇʟᴇᴛᴇ ᴄʜᴀᴛ
3. ᴊɪᴋᴀ ᴍᴀsɪ ɴɢɢᴀ ᴘᴇʀᴄᴀʏᴀ sᴀᴍᴀ ʙᴏᴛ ɪɴɪ ɴɢɢᴀ ᴜsᴀʜ ᴘᴀᴋᴇ ɴɢᴇɴᴛᴏᴛ.

**Still Command** ? 
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ ᴘʏʀᴏɢʀᴀᴍ ( ᴇᴠᴇɴ ᴠᴇʀsɪᴏɴ 𝟸 ) ᴅᴀɴ sᴇsɪ sᴛʀɪɴɢ ᴛᴇʟᴇᴛʜᴏɴ. ɢᴜɴᴀᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍᴘᴇʟᴀᴊᴀʀɪ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ.. 

**Developer** : @itsdaps 
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

sᴇʙᴜᴀʜ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘʏʀᴏɢʀᴀᴍ ᴅᴀɴ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @stringdap_bot

Group Support : [ɢᴀʙᴜɴɢ ᴋᴏɴᴛᴏʟ](https://t.me/privatedap)

Framework : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Language : [ᴘʏᴛʜᴏɴ](www.python.org)

Developer : @itsdaps
    """
