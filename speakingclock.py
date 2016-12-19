import logging
from time import gmtime, strftime

from opsdroid.skills import match_crontab

@match_crontab('* * * * *')
async def speaking_clock(opsdroid):
    logging.debug("Running speaking clock")
    connector = opsdroid.default_connector
    message = Message("placeholder", connector.default_room, None, connector)
    await message.respond(strftime("The time is now %H:%M", gmtime()))
