''' Task23. Напишите программу, которая найдёт произведение пар чисел списка.
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    (Сделать с использованием ф-ций: lambda, filter, map, zip, enumerate, list comprehension)

    Пример:
        2 3 4 5 6 => [12, 15, 16];
        2, 3, 5, 6 => [12, 15]
'''

# map
list_num = list(map(int, input('Введите числа через пробелы: ').split()))
n = (len(list_num) // 2) + [0, 1][len(list_num) % 2]

# list comprehension
list_new = [list_num[i] * list_num[-1 - i] for i in range(n)]

print('Произведение пар чисел списка равна:', list_new)
