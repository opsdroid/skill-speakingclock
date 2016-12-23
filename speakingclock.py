from time import gmtime, strftime

from opsdroid.skills import match_crontab, match_regex
from opsdroid.message import Message

@match_crontab('0 * * * *')
@match_regex(r"what time is it\?")
async def speaking_clock(opsdroid, message):

    # Get the default connector
    connector = opsdroid.default_connector

    # Create an empty message to respond to if triggered by the crontab
    if message is None:
        message = Message("", None, connector.default_room, connector)

    # Respond with the current time
    await message.respond(strftime("The time is now %H:%M", gmtime()))
