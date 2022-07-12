import telebot

def bot(way): bot = telebot.TeleBot((open(way).read().split('\n'))[0]); open(way).close(); return bot

def old_admin(way):
    users = open(way).read().split('\n')
    adm = []
    for i in range(len(users)): adm.append(users[i])
    open(way).close()
    return adm

bot = bot('inside/bot.txt')
adm = old_admin('inside/adm.txt')