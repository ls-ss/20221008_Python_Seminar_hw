''' Task15. Напишите программу, которая принимает на вход число N и выдает набор
    произведений чисел от 1 до N.
    Пример:
        пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
list =[]
temp = 1
for i in range( 1, int(input('Введите натуральное число: ')) + 1 ):
    temp *= i
    list.append(temp)
print(list)
