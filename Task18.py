''' Task18. Реализуйте алгоритм перемешивания списка.
'''

# Для генерации случайных данных импортируем модуль random
import random as rd

num = int(input('Введите длину списка целых чисел: '))
list_num = []
for i in range(num):
    list_num.append(i)
print('Созданный упорядоченный список: ', list_num)

for i in range(len(list_num)):
    n = rd.randint(0, len(list_num) - 1)
    list_num[i], list_num[n] = list_num[n], list_num[i]
print('Перемешанный список: ', list_num)

