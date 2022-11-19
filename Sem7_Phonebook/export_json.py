# Ф-ция преобразования телефонного справочника из CSV в JSON формат'
import pandas as pd
# from dicttoxml import dicttoxml
from create_phonebook_csv import phonebook_csv

def df_json():
    df = pd.read_csv(phonebook_csv, sep=',', header=None, encoding='utf-8')
    df = df[1:]  # Удаляем заголовок
    df.columns = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
    df.to_json('phonebook.json', orient='index', force_ascii=False)

    return True