"""
anah.py - Sopel Additions for Churches
Copyright © 2018, Joshua Burkholder, Calvary Bible Church
Licensed under the MIT License
"""

# sure...I could do all this statically, but where's the fun in that? :-P
from sopel import module
anah_version = "0.320.1350"

class language_data:
    name = ""
    greeting = ""
    conjunction = ""
    meetings = {}
    addressbook = {}
    phonebook = {}
    emailbook = {}

language_pack = {
    "en": language_data(),
    "es": language_data()
    }

## English
language_pack["en"].name = "English"
language_pack["en"].greeting = "Hello"
language_pack["en"].conjunction = "and"
language_pack["en"].meetings = {
    "Sundays at": ["10:00 am","11:15 am","7:00 pm"],
    "Wednesdays at": ["7:00 pm"]
    }
language_pack["en"].addressbook = {
    "Mailing Address": "P.O. Box 131, Wilkes-Barre, PA 18704",
    "Physical Address": "186 Sambourne Street, Wilkes-Barre, PA 18704"
    }
language_pack["en"].phonebook = {
    "Office": "570-824-5868"
    }
language_pack["en"].emailbook = {
    "Office": "church@calvarybiblewb.org",
    "Pastor": "pastor@calvarybiblewb.org"
    }

## Español
language_pack["es"].name = "Español"
language_pack["es"].greeting = "Hola"
language_pack["es"].conjunction = "y"
language_pack["es"].meetings = {
    "Domingos a las": ["10:00 am","11:15 am","7:00 pm"],
    "Miercoles a las": ["7:00 pm"]
    }
language_pack["es"].addressbook = {
    "Mailing Address": "P.O. Box 131, Wilkes-Barre, PA 18704",
    "Physical Address": "186 Sambourne Street, Wilkes-Barre, PA 18704"
    }
language_pack["es"].phonebook = {
    "Office": "570-824-5868"
    }
language_pack["es"].emailbook = {
    "Office": "iglesia@calvarybiblewb.org",
    "Pastor": "pastor@calvarybiblewb.org"
    }

def get_meetings(lang):
    meetings = language_pack[lang].meetings
    out_msg = ""
    for day in meetings:
        out_msg = out_msg + day
        if len(meetings[day]) == 1:
            out_msg = "{} {}".format(out_msg, meetings[day][0])
        elif len(meetings[day]) == 2:
            out_msg = "{} {} {} {}".format(out_msg, meetings[day][0], language_pack[lang].conjunction, meetings[day][1])
        else:
            out_msg = out_msg + " " + ', '.join(map(str, meetings[day][0:-1]))
            out_msg = "{}, {} {}".format(out_msg, language_pack[lang].conjunction, meetings[day][-1]
        out_msg = out_msg + ". "
    return out_msg

@module.rule('(.*time.*(service|meeting).*)|(.*(service|meeting).*time.*)')
def meetings_en(bot, trigger):
    bot.say(get_meetings("en"))

@module.rule('(.*hora.*(servicio|reunion).*)|(.*(servicio|reunion).*hora.*)')
def meetings_es(bot, trigger):
    bot.say(get_meetings("es"))

@module.commands('anah')
def get_anah_version(bot, trigger):
    bot.reply('The current anah version is %s' % anah_version)
