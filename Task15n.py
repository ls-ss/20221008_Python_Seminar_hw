''' Task15. Напишите программу, которая принимает на вход число N и выдает набор
    произведений чисел от 1 до N.
    (Сделать с использованием ф-ций: lambda, filter, map, zip, enumerate, list comprehension)
    Пример:
        пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

def mult_n(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp

# map
print(list(map(mult_n, range(1, int(input('Введите натуральное число: ')) + 1))))
