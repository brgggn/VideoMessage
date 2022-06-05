#для управления ботом
from book import *
import os
import os.path
import telebot
from telebot import types
user_chek = 0

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
try:
    os.mkdir("user")
except: pass

#________________________
# keyboard
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    file = f'user/{str(message.chat.id)}'

    if (os.path.exists(file)):
        markup.row(types.KeyboardButton(keyboard_1('video_bot')), types.KeyboardButton(keyboard_1('del_ch')))
        markup.row(types.KeyboardButton(keyboard_1('about')))
        bot.send_message(message.chat.id, mes_txt('keyboard'), reply_markup=markup)

    else:
        markup.row(types.KeyboardButton(keyboard_1('about')))
        bot.send_message(message.chat.id, mes_txt('start'), reply_markup=markup)

#________________________
@bot.message_handler(commands=['start'])
def start(message):
    keyboard(message)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, mes_txt('help'))

    bot.send_photo(message.chat.id, open('inside/1.png', 'rb'))
    open('inside/1.png', 'rb').close()

    bot.send_photo(message.chat.id, open('inside/2.png', 'rb'))
    open('inside/2.png', 'rb').close()

@bot.message_handler(content_types=['text'])
def textmessages(message):
    if (message.text.lower() == '101'):
        bot.send_message(message.from_user.id, f'101\n/{message.text}')

    elif((message.text.lower())[0] == '@'):
        file = open(f'user/{message.chat.id}', 'w')
        file.write(message.text.lower())
        file.close()

        bot.send_message(message.chat.id, mes_txt('add_ch') + message.text.lower())
        keyboard(message)

    elif(message.text.lower() == keyboard_1('about')):
        bot.send_message(message.chat.id, mes_txt('about'))

    elif (message.text.lower() == keyboard_1('video_bot')):
        bot.send_message(message.chat.id, mes_txt('video_bot'))
        global user_chek
        user_chek = 1

    elif (message.text.lower() == keyboard_1('del_ch')):
        os.remove(f'user/{str(message.chat.id)}')
        bot.send_message(message.chat.id, mes_txt('del_ch'))

        keyboard(message)

    else:
        bot.send_message(message.from_user.id, mes_txt('bag'))

@bot.message_handler(content_types=['document', 'photo', 'video', 'video_note'])
def file(message):
        content = message.content_type
        if content == 'photo':
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        elif content == 'document':
            file_info = bot.get_file(message.document.file_id)
        elif content == 'video':
            file_info = bot.get_file(message.video.file_id)
        elif content == 'video_note':
            file_info = bot.get_file(message.video_note.file_id)

        downloaded_file = bot.download_file(file_info.file_path)

        name_file = str(file_info.file_path.split('/')[1])

        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)

        with open(name_file, 'rb') as file:
            n_file = file.read()

        user = f'user/{str(message.chat.id)}'

        global user_chek
        if(user_chek == 1):
            bot.send_video_note(message.chat.id, n_file)
            user_chek = 0

            bot.send_message(message.from_user.id, mes_txt('user_chek') + (open(f'user/{str(message.chat.id)}').read().split('\n'))[0])

        elif(os.path.exists(user)):
            txt = open(f'user/{str(message.chat.id)}').read().split('\n')
            chanal = txt[0]
            try:
                bot.send_video_note(chanal, n_file)
                bot.send_message(message.from_user.id, mes_txt('good'))

            except:
                bot.send_message(message.from_user.id, mes_txt('e'))

        else:
            bot.send_video_note(message.chat.id, n_file)

        file.close()
        os.remove(name_file)


#________________________
bot.polling(none_stop=True)