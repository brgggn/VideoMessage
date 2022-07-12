from key import *

#________________________
#
while True:
     try:
         for i in range(len(adm)): bot.send_message(adm[i], '/start')

         exec(open('main.py').read())

     except Exception as e:
        for i in range(len(adm)): bot.send_message(adm[i], e)
