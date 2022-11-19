# Ф-ция ввода нового контакта в телефонную книгу.
# Формат ввода: Фамилия, Имя, Телефон (+7-xxx-xxx-xx-xx или 8-xxx-xxx-xx-xx ), Описание.
# Проверка третьего элемента списка (Номер телефона) на соответствие формату.
import re
import csv
from create_phonebook_csv import phonebook_csv

def write():
    print('Введите через пробел: Фамилию, Имя, Телефон (+7-xxx-xxx-xx-xx или 8-xxx-xxx-xx-xx ), Описание:')
    new_contact = list(map(str, input().split()))

    if len(new_contact) != 4:
        print('Ошибка: нужно заполнить 4 поля контакта: Фамилию, Имя, Телефон, Описание.')
        return False
    else:
        phone_pattern = re.compile('(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
        if phone_pattern.search(new_contact[2]):
            with open(phonebook_csv, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(new_contact)  # Создем заголовок таблицы для Phonebook.csv
                print('Создана новая запись в телефонной книге')
            return True
        else:
            print('Ошибка: Номер телефона не соответствует формату.')
            return False
