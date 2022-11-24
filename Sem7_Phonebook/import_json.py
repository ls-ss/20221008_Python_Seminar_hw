# Ф-ция преобразования телефонного справочника из JSON в CSV формат'
import json
import csv
from create_phonebook_csv import phonebook_csv

def add_json_csv():
    json_phonebook = 'phonebook_other.json'

    with open(json_phonebook, encoding='utf-8') as json_file:
        data = json.load(json_file)
        print('data= ', data)

    txt = json.dumps(data, ensure_ascii=False, indent=4)
    print('Содержимое импортированного json-файла:')
    print(txt)

# Добавляем записи из импортируемого json в phonebook_csv
    with open(phonebook_csv, 'a', newline='', encoding='utf-8') as f:
        for line in data:
            line_dict = data.get(line)
            contact = line_dict.get('Фамилия') + ',' + line_dict.get('Имя') + ',' + line_dict.get('Номер телефона') + ',' + line_dict.get('Описание')
            print('contact= ', contact)
            f.write(contact + '\n')

    print('Произведен импорт json-файл в телефонную книгу.')
    return True
