from key import *

#________________________
#
while True:
     try:
         for i in range(len(adm)): bot.send_message(adm[i], '/start')
         exec(open('main.py').read())

     except Exception as e:
         if (str(e) == "name 'e' is not defined"):
             for i in range(len(adm)): bot.send_message(adm[i], "ошибочка вышла)")

         else:
             for i in range(len(adm)): bot.send_message(adm[i], e)
