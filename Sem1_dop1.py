''' Дополнительная задача. Sem1_dop1.
    Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
        до минуты: <s> сек;
        до часа: <m> мин <s> сек;
        до суток: <h> час <m> мин <s> сек;
      * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

    Примеры:
        duration = 53
            53 сек
        duration = 153
            2 мин 33 сек
        duration = 4153
            1 час 9 мин 13 сек
        duration = 400153
            4 дн 15 час 9 мин 13 сек
'''

duration = int(input('Введите кол-во секунд: '))
minute = 60
hour = 60 * minute
day = 24 * hour

while duration >= minute:
    if duration >= day:
        temp = duration // day
        print( temp, 'дн', end=' ' )
        duration = duration - temp * day
    elif duration >= hour:
        temp = duration // hour
        print(temp, 'час', end=' ')
        duration = duration - temp * hour
    else:
        temp = duration // minute
        print(temp, 'мин', end=' ')
        duration = duration - temp * minute

print(duration, 'сек')
