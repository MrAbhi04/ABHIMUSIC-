
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, PING_IMG_URL
from ABHIMUSIC import app
from ABHIMUSIC.core.call import ABHI
from ABHIMUSIC.utils import bot_sys_stats
from ABHIMUSIC.utils.decorators.language import language
from ABHIMUSIC.utils.inline import support_group_markup


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await ABHI.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
        ),
        reply_markup=support_group_markup(_),
    )
