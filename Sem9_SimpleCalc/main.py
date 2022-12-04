import telebot
from telebot import types
import random as rd
from log import log

#global num1, num2, num3
#global a, b, n

# Токен Телеграм-бота
TOKEN = None
with open("token.txt") as f:
    TOKEN = f.read().strip()
bot = telebot.TeleBot(TOKEN)

# Имя для бота. Нужно в том случае, если обращаться к боту по имени
BOT_NAME = 'calc_bot'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text="Сложение", callback_data='add')
    sub = types.InlineKeyboardButton(text="Вычитание", callback_data='sub')
    multi = types.InlineKeyboardButton(text="Умножение", callback_data='multi')
    kb.add(add, sub, multi)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Сыграй в угадай число!".format(
                                                            message.from_user), reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
# Режим суммирования
    if callback.data == 'add':
        global num1, num2, num3
        num1 = num2 = num3 = -999
        global a, b, n
        a = rd.randint(-100, 100)
        b = rd.randint(0, 100)
        n = rd.randint(1, 3)

        while num1 == a + b or num1 == -999:
            num1 = rd.randint(-100, 200)
        while num2 == a + b or num2 == -999:
            num2 = rd.randint(-100, 200)
        while num3 == a + b or num3 == -999:
            num3 = rd.randint(-100, 200)

        n = rd.randint(1, 3)
        if n == 1:
            num1 = a + b
        elif n == 2:
            num2 = a + b
        else:
            num3 = a + b

        print(f'num1= {num1}, num2= {num2}, num3= {num3}, n= {n}')
        kb = types.InlineKeyboardMarkup(row_width=1)
        sum1 = types.InlineKeyboardButton(text=str(num1), callback_data='sum1')
        sum2 = types.InlineKeyboardButton(text=str(num2), callback_data='sum2')
        sum3 = types.InlineKeyboardButton(text=str(num3), callback_data='sum3')
        kb.add(sum1, sum2, sum3)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Сколько будет {a} + {b} ?', reply_markup=kb)

    txt = ''
    txt2 = ''

# Обработка ответов
    if callback.data == 'sum1':
        txt = 'Сложение: ' + str(a) + ' + ' + str(b) + '. Ваш ответ: '
        if n == 1:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num1)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a + b}.')
            txt += str(num1)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a + b) + '.'
            log(txt, txt2)

    if callback.data == 'sum2':
        txt = 'Сложение: ' + str(a) + ' + ' + str(b) + '. Ваш ответ: '
        if n == 2:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num2)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a + b}.')
            txt += str(num2)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a + b) + '.'
            log(txt, txt2)

    if callback.data == 'sum3':
        txt = 'Сложение: ' + str(a) + ' + ' + str(b) + '. Ваш ответ: '
        if n == 3:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num3)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a + b}.')
            txt += str(num3)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a + b) + '.'
            log(txt, txt2)

# Режим вычитания
    if callback.data == 'sub':
#        global num1, num2, num3
        num1 = num2 = num3 = -999

#        global a, b, n
        a = rd.randint(-100, 100)
        b = rd.randint(0, 100)
        n = rd.randint(1, 3)

        while num1 == a - b or num1 == -999:
            num1 = rd.randint(-100, 200)
        while num2 == a - b or num2 == -999:
            num2 = rd.randint(-100, 200)
        while num3 == a - b or num3 == -999:
            num3 = rd.randint(-100, 200)

        n = rd.randint(1, 3)
        if n == 1:
            num1 = a - b
        elif n == 2:
            num2 = a - b
        else:
            num3 = a - b

        print(f'num1= {num1}, num2= {num2}, num3= {num3}, n= {n}')
        kb = types.InlineKeyboardMarkup(row_width=1)
        sub1 = types.InlineKeyboardButton(text=str(num1), callback_data='sub1')
        sub2 = types.InlineKeyboardButton(text=str(num2), callback_data='sub2')
        sub3 = types.InlineKeyboardButton(text=str(num3), callback_data='sub3')
        kb.add(sub1, sub2, sub3)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Сколько будет {a} - {b} ?', reply_markup=kb)

    txt = ''
    txt2 = ''

# Обработка ответов
    if callback.data == 'sub1':
        txt = 'Вычитание: ' + str(a) + ' - ' + str(b) + '. Ваш ответ: '
        if n == 1:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num1)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a - b}.')
            txt += str(num1)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a - b) + '.'
            log(txt, txt2)

    if callback.data == 'sub2':
        txt = 'Вычитание: ' + str(a) + ' - ' + str(b) + '. Ваш ответ: '
        if n == 2:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num2)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a - b}.')
            txt += str(num2)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a - b) + '.'
            log(txt, txt2)

    if callback.data == 'sub3':
        txt = 'Вычитание: ' + str(a) + ' - ' + str(b) + '. Ваш ответ: '
        if n == 3:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num3)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a - b}.')
            txt += str(num3)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a - b) + '.'
            log(txt, txt2)

# Режим умножения
    if callback.data == 'multi':
        num1 = num2 = num3 = -999

        a = rd.randint(-10, 10)
        b = rd.randint(-10, 10)
        n = rd.randint(1, 3)

        while num1 == a * b or num1 == -999:
            num1 = rd.randint(-10, 10)
        while num2 == a * b or num2 == -999:
            num2 = rd.randint(-10, 10)
        while num3 == a * b or num3 == -999:
            num3 = rd.randint(-10, 10)

        n = rd.randint(1, 3)
        if n == 1:
            num1 = a * b
        elif n == 2:
            num2 = a * b
        else:
            num3 = a * b
        print(f'num1= {num1}, num2= {num2}, num3= {num3}, n= {n}')

        kb = types.InlineKeyboardMarkup(row_width=1)
        multi1 = types.InlineKeyboardButton(text=str(num1), callback_data='multi1')
        multi2 = types.InlineKeyboardButton(text=str(num2), callback_data='multi2')
        multi3 = types.InlineKeyboardButton(text=str(num3), callback_data='multi3')
        kb.add(multi1, multi2, multi3)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'Сколько будет {a} * {b} ?', reply_markup=kb)

    txt = ''
    txt2 = ''

# Обработка ответов
    if callback.data == 'multi1':
        txt = 'Умножение: ' + str(a) + ' * ' + str(b) + '. Ваш ответ: '
        if n == 1:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num1)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a * b}.')
            txt += str(num1)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a * b) + '.'
            log(txt, txt2)

    if callback.data == 'multi2':
        txt = 'Умножение: ' + str(a) + ' * ' + str(b) + '. Ваш ответ: '
        if n == 2:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num2)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a * b}.')
            txt += str(num2)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a * b) + '.'
            log(txt, txt2)

    if callback.data == 'multi3':
        txt = 'Умножение: ' + str(a) + ' * ' + str(b) + '. Ваш ответ: '
        if n == 3:
            bot.send_message(callback.message.chat.id, f'Правильно!')
            txt += str(num3)
            log(txt, 'Правильно!')
        else:
            bot.send_message(callback.message.chat.id, f'Не угадал. Правильный ответ: {a * b}.')
            txt += str(num3)
            txt2 = 'Не угадал. Правильный ответ: ' + str(a * b) + '.'
            log(txt, txt2)


if __name__ == '__main__':
     bot.infinity_polling() # Чтобы бот старался не прекращать работу

'''    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Нажмите на нужную кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Кнопка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, 'Спасибо за прочтение статьи!')

# bot.infinity_polling() # Чтобы бот старался не прекращать работу

'''
