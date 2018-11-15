"""
anah.py - Basic Anah Functionality for Sopel
Copyright 2018, Joshua Burkholder, CalvaryBibleWB.org
Licensed under the MIT License.

This module is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by Sopel.

https://sopel.chat
"""

import sopel.module
anah_version = '0.319.1100'

@sopel.module.commands('anah')
def modver(bot, trigger):
    bot.reply('The main anah module is at version ' + anah_version)

#Convert static data into dynamic

@sopel.module.rule('.*(time.*(service|meeting))|((service|meeting).*time).*')
def hours_en(bot, trigger):
    bot.say('Sundays at 10:00a, 11:15a, and 7:00p. Wednesdays at 7:00p.')

@sopel.module.rule('.*(hora.*(servicio|reunion))|((servicio|reunion).*hora).*')
def horas_es(bot, trigger):
    bot.say('Domingos a las 10:00a, 11:15a, y 7:00p. Miercoles a las 7:00p.')
