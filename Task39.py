''' Task39. Создайте программу для игры с конфетами человек против человека.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
    чтобы забрать все конфеты у своего конкурента?
        a) Добавьте игру против бота
        b) Подумайте как наделить бота ""интеллектом""
'''
import random as rd

def input_num():
    in_num = 29
    while (in_num > candies) or (in_num < 1 or in_num > 28):
        in_num = int(input())

        if(in_num > candies) or (in_num < 1 or in_num > 28):
            print('Ввели недопустимое число:')
            if in_num > candies:
                print(f' -Введенное число {in_num} больше оставшихся конфет {candies}')
            if in_num < 1 or in_num > 28:
                print(f' -Введенное число {in_num} выходит за пределы допустимого диапазона: 1..28')
            print('Введите число еще раз: ', end='')
            continue
    return in_num


mode = int(input('Выберите режим игры (0 - игра вдвоем, 1 - против бота): '))

candies = 2021 # Кол-во конфет
# Выбираем, кто будет ходить первым
gamer = bool(rd.choice([True, False])) # True - Вы, False - соперник
print('Ваш ход первый' if gamer else 'Первым ходит соперник')

while candies > 0:
    print(f' *Кол-во конфет: {candies}')
    if gamer:           # Ваш ход
        print('Ваш ход (введите число 1..28): ', end='')
        num = input_num()
    else:               # Ход соперника
        if not(mode):       # Игра вдвоем
            print('Ход соперника: ', end='')
            num = input_num()
        else:               # Игра против бота
            if candies <= 28:
                num = candies
            elif not(candies % 28):
                num = 27
            else:
                num = candies - 28 * (candies // 28) - 1
            print('Ход бота: ', num)

    candies -= num
    gamer = not(gamer)

gamer = not(gamer)
print('Вы победили!' if gamer else 'Победил соперник!')
