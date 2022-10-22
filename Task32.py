''' Task32. Задайте последовательность чисел. Напишите программу, которая
    выведет список неповторяющихся элементов исходной последовательности.
'''
list_num = [2, 4, 5, 7, 1, 2, 15, 2, 2, 1, 5, 0]

print(list(set(list_num))) # Первый вариант используя ф-цию set

# Второй вариант
list_new = []
while len(list_num):
    min_num = min(list_num)
    list_new.append(min_num)
#    print(list_num, list_new)

    while list_num.count(min_num) > 0:
        list_num.remove(min_num)

print(list_new)
