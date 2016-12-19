from time import gmtime, strftime

from opsdroid.skills import match_crontab

@match_crontab('* * * * *')
async def speaking_clock(opsdroid):
    await message.respond(strftime("The time is now %H:%M", gmtime()))
