import telebot
import emoji
import random

with open('key.txt',encoding="utf-8") as file:
    f = file.read()

API_KEY = str(f)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['welcome'])
def welcome(message):
    bot.reply_to(message,'welcome to suvoo-land')
# bot.polling()

@bot.message_handler(commands=['hullo'])
def hullo(message):
    bot.send_message(message.chat.id,'hullo noobs')

# @bot.message_handler(commands=['emo'])
# def hullo(message):
#     bot.send_message(message.chat.id,'hullo noobs')


def emojy(words):
    words = words[1:]

    options = [ emoji.UNICODE_EMOJI_ENGLISH, emoji.UNICODE_EMOJI_ALIAS_ENGLISH,
            emoji.UNICODE_EMOJI_ITALIAN,emoji.UNICODE_EMOJI_SPANISH,
            emoji.UNICODE_EMOJI_PORTUGUESE  ]

    choi = random.choice(options)
    emo = []
    for i in choi:
        emo.append(i)
    ans = ''
    for w in words:
        # print(w,' ',random.choice(emo))
        ans += w + ' ' + random.choice(emo)
    return ans

def custom_emoj(message):
    request = message.text.split(' ')
    if len(request) >= 2:
        return True
    elif request[0] != 'emo':
        return False

@bot.message_handler(func=custom_emoj)
def actual_emoj(message):
    words = message.text.split(' ')
    if words[0] != 'emo':
        bot.send_message(message.chat.id,'change format please')
    else:
        ans = emojy(words)
        print(ans)
        bot.send_message(message.chat.id,ans)
        # bot.reply_to(message,ans)

bot.polling()

