''' Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах
    (CSV, JSON, XML).
'''
from help import help
from log import log
from create_phonebook_csv import create_phonebook_csv
from write import write
from read import read
from delete import delete
from export_json import df_json
from import_json import add_json_csv


# Ф-ция создаст телефонную книгу 'Phonebook.csv', если ее нет.
create_phonebook_csv()

while(True):
    print('Для просмотра инструкции по работе с командной строкой введите команду "СПРАВКА" (регистр символов не важен).')
    command = input('Командная строка: ')
    if command.lower() == 'справка':
        help()
        log('Вызов "СПРАВКИ"', 'ОК!')
        print('-' * 10)
    elif command.lower() == 'добавить':
        command = write()
        txt = 'ОК!' if command else 'ERROR!'
        log('Создание нового контакта', txt)
        print('-' * 10)
    elif command.lower() == 'найти':
        command = read()
        txt = 'ОК!' if command else 'ERROR!'
        log('Поиск контактов', txt)
        print('-' * 10)
    elif command.lower() == 'удалить':
        command = delete()
        txt = 'ОК!' if command else 'ERROR!'
        log('Удаление контактов', txt)
        print('-' * 10)
    elif command.lower() == 'json':
        command = df_json()
        txt = 'ОК!' if command else 'ERROR!'
        log('Преобразование в JSON', txt)
        print('-' * 10)
    elif command.lower() == 'import_json':
        command = add_json_csv()
        txt = 'ОК!' if command else 'ERROR!'
        log('Импорт из JSON', txt)
        print('-' * 10)
    else:
        print('Такой команды нет')
