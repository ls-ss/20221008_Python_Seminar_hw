''' Task22. Задайте список из нескольких чисел. Напишите программу, которая найдёт
    сумму элементов списка, стоящих на нечётной позиции.

    Пример:
        - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

list_num = list(map(int, input('Введите числа через пробелы: ').split()))
print('Сумма элементов списка на нечётных позициях равна:', sum(list_num[1::2]))
