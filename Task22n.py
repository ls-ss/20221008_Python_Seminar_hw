''' Task22. Задайте список из нескольких чисел. Напишите программу, которая найдёт
    сумму элементов списка, стоящих на нечётной позиции.
    (Сделать с использованием ф-ций: lambda, filter, map, zip, enumerate, list comprehension)

    Пример:
        - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

#list_num = [0, 1, 2, 3, 4, 5, 6, 7]
list_num = list(map(int, input('Введите числа через пробелы: ').split()))

summ = 0
for i in range(1, len(list_num), 2):
    summ += (lambda i: list_num[i])(i)

print('Сумма элементов списка на нечётных позициях равна: ', summ)
