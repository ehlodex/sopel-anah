"""
anah.py - Sopel Additions for Churches
Copyright © 2018, Joshua Burkholder
Licensed under the MIT License

Anah (an·ä') is a name that means 'one who answers' in Hebrew (Gen. 36, 1Ch 1)
Strong's Concordance with Hebrew and Greek Lexion: H6034
"""
from sopel import module
from sopel import __version__ as sopel_version
from datetime import datetime, timedelta
#anah_updated is future use. This will let people know the data might be old.
#anah_version is calulated based on the last updated date.
anah_updated = datetime.strptime('2018-11-19 14:21', '%Y-%m-%d %H:%M')
anah_version = '0.{}.{}{}'.format(anah_updated.timetuple().tm_yday, anah_updated.hour, anah_updated.minute)

#this needs to be broken into separate files (one for each language) then imported as language_pack
class language_data:
    name = ''
    greeting = ''
    conjunction = ''
    end_of_data = ''
    meetings = {}
    addressbook = {}
    phonebook = {}
    emailbook = {}

language_pack = {
    'en': language_data(),
    'es': language_data()
    }

## English
language_pack['en'].name = 'English'
language_pack['en'].greeting = 'Hello'
language_pack['en'].conjunction = 'and'
language_pack["en"].end_of_data = "That's everything that I have."
language_pack['en'].meetings = {
        'Sundays at': ['00:00','01:00','02:00'],
        'Wednesdays at': ['00:00']
        }
language_pack['en'].addressbook = {
        'Physical address': '123 Anyold Street, Somewhere',
        'Mailing address': 'Box 123, Somwhere'
        }
language_pack['en'].phonebook = {
        'Office': '(123) 456-7890'
        }
language_pack['en'].emailbook = {
        'Office': 'office@anah.module',
        'Pastor': 'pastor@anah.module'
        }

## Español
language_pack['es'].name = 'Español'
language_pack['es'].greeting = 'Hola'
language_pack['es'].conjunction = 'y'
language_pack['es'].end_of_data = 'Eso es todo lo que tengo.'
language_pack['es'].meetings = {
        'Domingos a las': ['00:00','01:00','02:00'],
        'Miercoles a las': ['00:00']
        }
language_pack['es'].addressbook = {
        'Direccion fisica': '123 Calle Anyold, Somewhere',
        'Direccion de envio': 'Box 123, Somewhere'
        }

# functions to separate data from the language_pack dictionaries.
# with a small rewrite, this can be a single function
# maybe needs to be included in the language pack itself, not anah.py
def get_meetings(lang):
    meetings = language_pack[lang].meetings
    out_msg = ''
    for day in meetings:
        out_msg = out_msg + day
        if len(meetings[day]) == 1:
            out_msg = '{} {}'.format(out_msg, meetings[day][0])
        elif len(meetings[day]) == 2:
            out_msg = '{} {} {} {}'.format(out_msg, meetings[day][0], language_pack[lang].conjunction, meetings[day][1])
        else:
            out_msg = out_msg + ' ' + ', '.join(map(str, meetings[day][0:-1]))
            out_msg = '{}, {} {}'.format(out_msg, language_pack[lang].conjunction, meetings[day][-1])
        out_msg = out_msg + '. '
    return out_msg

def get_addresses(bot, trigger, lang):
    addresses = language_pack[lang].addressbook
    for address in addresses:
        bot.say('{}: {}'.format(address, addresses[address]))
    bot.say(language_pack[lang].end_of_data)
    return None

# Comtrya! Actions for the Sopel bot!
@module.nickname_commands('version')
def get_anah_version(bot, trigger):
    bot.reply('Sopel v. %s with Anah v. %s' % (sopel_version, anah_version))

# the regex syntax might get moved into the language_pack data.
# This would make them more independent and allow for more modular usage

@module.rule('(.*time.*(service|meeting).*)|(.*(service|meeting).*time.*)')
def meetings_en(bot, trigger):
    bot.say(get_meetings('en'))

@module.rule('(.*hora.*(servicio|reunion).*)|(.*(servicio|reunion).*hora.*)')
def meetings_es(bot, trigger):
    bot.say(get_meetings('es'))

@module.rule('.*address.*')
def address_en(bot, trigger):
    get_addresses(bot, trigger, 'en')

@module.rule('.*direccion.*')
def address_es(bot, trigger):
    get_addresses(bot, trigger, 'es')
    
# add rules for phone numbers and email addresses
# add rules/commands for groups of similar data (e.g. all 'Office' contact information)

# Data separation needs some (read: 'a lot of') work, so the structure may change significantly
