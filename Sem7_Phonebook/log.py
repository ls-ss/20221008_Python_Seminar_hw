# Ф-ция создания и введения журнала событий и действий.
from os.path import exists
import datetime

log_file = 'log.txt'

def log(some_str, result):
    if not exists(log_file):
        # Создем файл log.txt
        with open(log_file, mode='w', encoding="utf-8") as f:
            f.write('Журнал событий телефонного справочника.' + '\n')

    with open(log_file, mode='a', encoding="utf-8") as f:
        f.write(f'{some_str} = {result} Время события: {datetime.datetime.now()}' + '\n')
