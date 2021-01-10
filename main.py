import telebot
from parsing_module import lastCardResult, getTournamentResult, figterRecord
from data import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome_handler(message):
    bot.send_message(message.from_user.id, 
    '''Hello, You can control me with this commands:\n
    /help - to see all commands
    /lastcard - to see last tournament results''')
    # /cardnumber - to see tournaments results
    # /fighter - to see fighter record


@bot.message_handler(func=lambda  m: True)
def command_handler(message):
    if message.text == '/lastcard':
        bot.send_message(message.from_user.id, 'Last card results:\n\n' + lastCardResult())
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 
        '''You can control me with this commands:\n
    /help - to see all commands
    /lastcard - to see last card results''')
    # /cardnumber - to see results of chosen card
    # /fighter - to see fighter record
    # elif message.text == '/cardnumber':
    #     bot.send_message(message.from_user.id, 'Enter the tournament number:')
    #     bot.register_next_step_handler(message, tournamentResult)
    # elif message.text == '/fighter':
    #     bot.send_message(message.from_user.id, 'Enter fighter\'s name:')
    #     bot.register_next_step_handler(message, fighterStat)


def tournamentResult(message):
    tournamentNumber = message.text
    bot.send_message(message.from_user.id, 'vot tebe ' + getTournamentResult(tournamentNumber))


def fighterStat(message):
    fighter = message.text
    bot.send_message(message.from_user.id, 'vot tebe ' + figterRecord(fighter))


bot.polling()