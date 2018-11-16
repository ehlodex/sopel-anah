"""
anah.py - Basic Anah Functionality for Sopel
Copyright 2018, Joshua Burkholder, CalvaryBibleWB.org
Licensed under the MIT License.

This module is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by Sopel.

https://sopel.chat
"""

import sopel.module
anah_version = '0.319.1100'

# Meeting Times
## STATIC - Not yet converted
services = {
    "en": {"Sundays": ["10:00 am","11:15 am","7:00 pm"], "Wednesdays": ["7:00 pm"]},
    "es": {"Domingos": ["10:00 am","11:15 am","7:00 pm"], "Miercoles": ["7:00 pm"]}
}

@sopel.module.commands('anah')
def modver(bot, trigger):
    bot.reply('The main anah module is at version ' + anah_version)

@sopel.module.rule('.*(time.*(service|meeting))|((service|meeting).*time).*')
def hours_en(bot, trigger):
    # you can add a message prefix here
    services_msg = ""
    days = services["en"]
    for day in days:
        if len(days[day]) == 1:
            day_msg = day + " at " + days[day][0]
        elif len(days[day]) == 2:
            day_msg = day + " at " + days[day][0] + " and " + days[day][1]
        else:
            day_msg = day + " at " + ', '.join(days[day][0:-1]) + ", and " + days[day][-1]
        day_msg = day_msg + ". "
        services_msg = services_msg +  day_msg
    bot.say(services_msg)

@sopel.module.rule('.*(hora.*(servicio|reunion))|((servicio|reunion).*hora).*')
def hours_en(bot, trigger):
    # you can add a message prefix here
    services_msg = ""
    days = services["es"]
    for day in days:
        if len(days[day]) == 1:
            day_msg = day + " at " + days[day][0]
        elif len(days[day]) == 2:
            day_msg = day + " at " + days[day][0] + " and " + days[day][1]
        else:
            day_msg = day + " at " + ', '.join(days[day][0:-1]) + ", and " + days[day][-1]
        day_msg = day_msg + ". "
        services_msg = services_msg +  day_msg
    bot.say(services_msg)
