# Ф-ция поиска контактов из phonebook_csv по 'Фамилии' или по 'Фамилии и Имени'
import pandas as pd
from create_phonebook_csv import phonebook_csv

def read():
    print('Нажатие Enter без ввода значения выведет все контакты')
    print('Введите "Фамилию" или "Фамилию Имя": ')
    key_word = []
    key_word = list(map(str, input().split()))

    df = pd.read_csv(phonebook_csv, sep=',', header=None)
    df = df[1:]     # Удаляем заголовок
    df.columns = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']

    if len(key_word) == 0:
        print(df)
        return True
    elif len(key_word) == 1:
        df_new = df.loc[df['Фамилия'] == key_word[0]]
        if df_new.shape[0]:
            print(df_new)
        else:
            print('Контакта с такой Фамилией нет.')
        return True
    elif len(key_word) == 2:
        df_new = df.loc[ (df['Фамилия'] == key_word[0]) & (df['Имя'] == key_word[1]) ]
        if df_new.shape[0]:
            print(df_new)
        else:
            print('Контакта с такой Фамилией и Именем нет.')
        return True
    else:
        print('Ошибка: Поиск осуществляется только по столбцам "Фамилия" или "Фамилия Имя".')
        return False
