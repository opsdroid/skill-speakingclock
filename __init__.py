# from time import gmtime, strftime
from datetime import datetime, timezone
import pytz

from opsdroid.matchers import match_crontab, match_regex
from opsdroid.message import Message


@match_crontab("0 * * * *")
@match_regex(r"what time is it\?")
async def speaking_clock(opsdroid, config, message):
    # Get the default connector
    connector = opsdroid.default_connector

    # If user has configured timezone under skill use it
    # otherwise use the configured timezone for opsdroid
    # if that isn't configured default to UTC
    local_tz = pytz.timezone(
        config.get("timezone", pytz.timezone(opsdroid.config.get("timezone", "UTC")))
    )
    show_utc = config.get("show_utc", False)

    ## See if user wants UTC or local configure
    local_time = datetime.now(tz=local_tz)
    utc_time = local_time.astimezone(tz=timezone.utc)

    if show_utc:
        timemsg = f'{utc_time.strftime("It is %H:%M [%Z]")}, {local_time.strftime("%H:%M [%Z]")}'
    else:
        timemsg = f'{local_time.strftime("%H:%M [%Z]")}'

    # Create an empty message to respond to if triggered by the crontab
    if message is None:
        message = Message("", None, connector.default_room, connector)
        response = f"The time is now {timemsg}"
    else:
        response = f"It is {timemsg}"

    await message.respond(response)
