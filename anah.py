from sopel import module
anah_version = "0.320.1331"

class language_data:
    name = ""
    greeting = ""
    meetings = {}

language_pack = {
    "en": language_data(),
    "es": language_data()
    }

## English
language_pack["en"].name = "English"
language_pack["en"].greeting = "Hello"
language_pack["en"].meetings = {
        "Sundays at": ["10:00 am","11:15 am","7:00 pm"],
        "Wednesdays at": ["7:00 pm"]
        }

## Español
language_pack["es"].name = "Español"
language_pack["es"].greeting = "Hola"
language_pack["es"].meetings = {
        "Domingos a las": ["10:00 am","11:15 am","7:00 pm"],
        "Miercoles a las": ["7:00 pm"]
        }

def get_meetings(lang):
    meetings = language_pack[lang].meetings
    out_msg = ""
    for day in meetings:
        out_msg = out_msg + day
        if len(meetings[day]) == 1:
            out_msg = out_msg + " " + meetings[day][0]
        elif len(meetings[day]) == 2:
            out_msg = out_msg + " " + meetings[day][0] + " and " + meetings[day][1]
        else:
            out_msg = out_msg + " " + ', '.join(map(str, meetings[day][0:-1]))
            out_msg = out_msg + ", and " + meetings[day][-1]
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
