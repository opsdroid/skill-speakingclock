from time import gmtime, strftime

from opsdroid.skills import match_crontab
from opsdroid.message import Message

@match_crontab('0 * * * *')
async def speaking_clock(opsdroid):

    # Get the default connector
    connector = opsdroid.default_connector

    # Create an empty message to respond to
    message = Message("", None, connector.default_room, connector)

    # Respond with the current time
    await message.respond(strftime("The time is now %H:%M", gmtime()))
