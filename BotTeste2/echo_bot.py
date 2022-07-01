import telebot
from telebot import types
import random
from random import randrange
from random import choice


TOKEN = '5415027263:AAGtaqQSPtsCeJAPVYfCwcbDyeJM35tT78k'
tb = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot("5415027263:AAGtaqQSPtsCeJAPVYfCwcbDyeJM35tT78k") # You can set parse_mode by default. HTML or MARKDOWN


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8];

captions = [
"🐱*Blake Belladonna*🐱\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 1",
"🐱*Blake Belladonna*🐱\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 4",
"🐱*Blake Belladonna*🐱\n *Raridade:* S\+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Menágerie \n *Raça:* Fauno \n *Volume:* 8",
"🦾*Yang Xiao long*🦾\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 1",
"🦾*Yang Xiao long*🦾\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 4",
"🦾*Yang Xiao long*🦾\n *Raridade:* S\+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Huamana \n *Volume:* 8",
"🌹*Ruby Rose*🌹\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 1",
"🌹*Ruby Rose*🌹\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 4",
"🌹*Ruby Rose*🌹\n *Raridade:* S\+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Patch Island \n *Raça:* Humana \n *Volume:* 8",
"❄*Weiss Schnee*❄\n *Raridade:* A \n *Filiação:* Beacon Academy \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Humana \n *Volume:* 1",
"❄*Weiss Schnee*❄\n *Raridade:* S \n *Filiação:* Ozpin \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Humana \n *Volume:* 4",
"❄*Weiss Schnee*❄\n *Raridade:* S\+ \n *Filiação:* Team RWBY \n *Time:* RWBY \n *Origem:* Atlas \n *Raça:* Huamana \n *Volume:* 8"
];
photos = [
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Blake_V1_A.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Blake_V4_S.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Blake_V7_S+.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Yang_V1_A.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Yang_V4_S.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Yang_V7_S+.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Ruby_V1_A.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Ruby_V4_S.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Ruby_V7_S+.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Weiss_V1_A.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Weiss_V4_S.png?raw=true',
    'https://github.com/iuripprata/atividades-sopr/blob/main/BotTeste2/cards/Weiss_V7_S+.png?raw=true',
];


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['blake'])
def sendphoto(message):
    i = int(randrange(len(numbers)))
    bot.send_photo(message.chat.id, photos[i],
                   caption=captions[i],
                   parse_mode='MarkdownV2')
    print(numbers[i], captions[i], i)

@bot.message_handler(commands=['teste'])
def start(message):
    "Sending Welcome to Bot Message"

    global user
    global chat
    global message_id

    if message.from_user.username is None:
        bot.send_message("Sorry! You are only qualified for a lucky draw if you have username.")
    else:
        chat = message.chat.id
        user = message.from_user
        message_id = message.message_id
        bot.reply_to(message, "qualified")



bot.polling(none_stop=True, timeout=60)

