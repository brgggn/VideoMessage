import telebot
#________________________
def bot():
    txt = open('inside/bot.txt').read().split('\n')
    global bot
    bot = telebot.TeleBot(txt[0])

    return 0

def adm():
    txt = open('inside/adm.txt').read().split('\n')
    global adm
    adm = txt[0]

    return 0

adm()
bot()
#________________________

while True:
     try:
         bot.send_message(adm, 'run')
         exec(open('VideoMessagebot.py').read())

     except Exception as e:
          bot.send_message(adm, e)






