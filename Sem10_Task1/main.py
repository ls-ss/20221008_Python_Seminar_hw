''' Семинар 10. Задача 1. Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и
    среднее арифметическое последовательности целых чисел.
    Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число, которое
    будет учтено при вычислении финального результата методом result. Для экземпляров MinStat и MaxStat result должен
    возвращать целое число, для AverageStat — число типа float (это число будет сравниваться с правильным ответом до
    седьмой значащей цифры).

    Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен
    возвращать None.

        Пример 1.
            values = [1, 2, 4, 5]

            mins = MinStat()
            maxs = MaxStat()
            average = AverageStat()
            for v in values:
                mins.add_number(v)
                maxs.add_number(v)
                average.add_number(v)

            print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

        Пример 2.
            mins = MinStat()
            maxs = MaxStat()
            average = AverageStat()

            print(mins.result(), maxs.result(), average.result())

        Пример 3.
            values = [1, 0, 0]

            mins = MinStat()
            maxs = MaxStat()
            average = AverageStat()
            for v in values:
                mins.add_number(v)
                maxs.add_number(v)
                average.add_number(v)

            print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
'''

import func_stat

# Примеры из задания
print("Пример 1:")
values = [1, 2, 4, 5]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

print("Пример 2:")
values = [1, 2, 4, 5]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
print(mins.result(), maxs.result(), average.result())

print("Пример 3:")
values = [1, 0, 0]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
