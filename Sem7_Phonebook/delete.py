# Ф-ция удаления контактов из phonebook_csv по 'Фамилии' или по 'Фамилии и Имени'
import pandas as pd
from create_phonebook_csv import phonebook_csv

def delete():
    print('Ввод значения: "ВСЕ" удалит телефонную книгу')
    print('Введите "Фамилию" или "Фамилию Имя": ')
    key_word = []
    key_word = list(map(str, input().split()))

    df = pd.read_csv(phonebook_csv, sep=',', header=None)
    df = df[1:]     # Удаляем заголовок
    df.columns = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']

    if len(key_word) == 1 and key_word[0].lower() == 'все':
        df.drop(df.index[:], inplace=True) # Очистили df
        df.to_csv(phonebook_csv, index=None)
        print('Все контакты удалены')
    elif len(key_word) == 1:
        df = df[df['Фамилия'].str.contains(key_word[0]) == False]
        df.to_csv(phonebook_csv, index=None)
        print(f'Контакты с фамилией: {key_word[0]} удалены')
        return True
    else:
        print('Ошибка: Проблема с удалением.')
        return False
