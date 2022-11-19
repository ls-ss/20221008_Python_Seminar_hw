''' Ф-ция создания новой телефонной книги если она отсутствует'''
from os.path import exists
import csv

phonebook_csv = 'Phonebook.csv'

def create_phonebook_csv():
    phonebook_header = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']

    if not exists(phonebook_csv):
        # Создем файл Phonebook.csv
        with open(phonebook_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(phonebook_header) # Создем заголовок таблицы для Phonebook.csv
