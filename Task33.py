''' Task33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

    Пример:
        k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random as rd
degree = int(input('Введите натуральную степень: '))
# Словарь преобразования цифр в степень
indexes_degree = { "0": "\u2070",
                   "1": "\u00B9",
                   "2": "\u00B2",
                   "3": "\u00B3",
                   "4": "\u2074",
                   "5": "\u2075",
                   "6": "\u2076",
                   "7": "\u2077",
                   "8": "\u2078",
                   "9": "\u2079",
                   "-": "\u207B"    }

# Ф-ция возвращает число в виде 'х' в степени 'n'
def Degree(n):
    temp = ''
    if n == 0:
        return ''
    elif n == 1:
        return 'x'
    else:
        for i in str(n):
            temp += indexes_degree[i]

    return 'x' + temp

# Организовываем цикл с кол-вом итераций равным введенному числу + 1,
# тем самым создавая члены многочлена (от самой высокой степени до степени 0).
num = 0
polynom = ''
for i in range(degree, -1, -1):
    # Проверяем, чтобы коэфф-т первого члена многочлена не был равен нулю
    if i == degree:
        while not(num):
            num = rd.randint(-100, 100)
    else:
        num = rd.randint(-100, 100)

    # Определяемся когда выводим '+', '-', или совсем ничего не выводим
    if num == 0:
        continue
    elif num > 0 and i != degree:
#        print(' + ', end='')
        polynom += ' + '
    elif num < 0:
#        print(' - ', end='')
        polynom += ' - '
    # Определяем когда ставить знак '*'
    if i == 0:
        temp = str(abs(num))
    elif abs(num) != 1:
        temp = str(abs(num))
        temp += '*' if i else ''
    else:
        temp = ''

#    print(f'{temp}{Degree(i)}', end='') # Выводим очередной член многочлена
    polynom += temp + Degree(i)
#print(' = 0')
polynom += ' = 0'
print(polynom)

# Создаем файл и записываем туда созданный многочлен
with open('task33_polynom.txt', mode='w', encoding="utf-8") as f:
    f.write(polynom)
