''' Task17. Задайте список из N элементов, заполненных числами
    из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
    Позиции хранятся в файле file.txt в одной строке одно число.

    Пример:
        Введите длину списка (число не менее 1-го): 5
    -->
        Созданный список:  [-1, 2, -5, 5, -1]
        Принятые индексы из файла:  [0, 2]
        Произведение элементов на указанных позициях равна: -1 * -5 = 5
'''
import random as rd
import os

# Ф-ция последовательного чтения из файла строк с числами, и возврата их как int
def read_file(n):
    with open('file.txt', 'r') as f:
        for i in range(n):
            f.readline()
        lines = f.readline()
    # Удаляем управляющий символ '\n' из строки, переводим 'str' в 'int' и возвращаем
    return int( lines.replace("\n", "") )


# Ф-ция создания файла file.txt и заполнения их строками с числами.
# Если такой файл уже существует, то предварительно его удаляет.
def create_file(n):
    # Если файл существует, то удаляем его
    if os.path.exists('file.txt'):
        os.remove('file.txt')

    # Создаем список чисел от 0...num и перемешиваем его
    lst = list(range(num))
    rd.shuffle(lst)

    with open('file.txt', 'w+') as f:
        for i in lst:
            f.write(str(i) + '\n')

# *** Начало! ***
num = int(input('Введите длину списка (число не менее 1-го): '))
# Создаем список из 'num' целых чисел со значениями '-num' до 'num'
list_num = [rd.randint(-num, num) for i in range(num)]
print('Созданный список: ', list_num)

create_file(num) # Создаем файл со списком чисел

# Считываем случайное число раз (от 1 и не более длины list_num) случайные строчки из файла file.txt
x = [] # Пустой список принятых индексов из файла
for i in range(rd.randint(1, num)):
    x.append(read_file(i))
print(f'Принятые индексы из файла: ', x)

# Перемножаем числа на указаных позициях
print(f'Произведение элементов на указанных позициях равна: ', end='')
multi = 1
for i in range(len(x)):
    print(f'{list_num[x[i]]}', end='')
    if i < len(x) - 1:
        print(end= ' * ')
    else:
        print(end= ' = ')
    multi = multi * list_num[x[i]]
print(multi)
