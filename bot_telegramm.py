import telebot
import requests
from bs4 import BeautifulSoup
import random


token = '5884673239:AAH9X1tzBLpesbJjZxloXbGjMHuRD-xVYmo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    print(message.from_user.id)


@bot.message_handler(commands=['fact'])
def get_fact(message):
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    get_fact = fact.text
    get_link = (fact.a.attrs['href'])
    bot.send_message(message.from_user.id, get_fact + get_link)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEJzA1kvkY2vh6Owk0H1cQG9oWycgbTFgAC5iwAAlh78EkcfK0XbF_dgC8E")


@bot.message_handler(commands=['pic'])
def get_fact(message):
    pic_num = str(random.randint(1, 4))
    picture = open('out (' + pic_num + ').jpg', 'rb')
    bot.send_photo(message.from_user.id, picture)


@bot.message_handler(content_types=['text'])
def get_test_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
        answers = ['Отлично', 'Прекрасно', 'Лучше не бывает', 'Хорошо, а как у вас?']
        get_answers = random.choice(answers)
        bot.send_message(message.from_user.id, get_answers)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю')


button1 = telebot.types.KeyboardButton('Button1')
button2 = telebot.types.KeyboardButton('Button2')

keyboard = telebot.types.ReplyKeyboardMarkup()

keyboard.add(button1, button2)


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == 'Button 2':
        id_image = random.randint(1, 4)
        my_random_img = open(f'Cats/{id_image}.jpg', 'rb')
        bot.send_photo(message.from_user.id, my_random_img)


bot.polling()
