''' Семинар 10. Задача 2. Реализуйте класс Table, который хранит целые числа в двумерной таблице.
    При инициализации Table (rows, cols) экземпляру передаются число строк и столбцов в таблице.
    Строки и столбцы нумеруются с нуля.
        table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col.
                                    Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.

        table.set_value(row, col, value) — записать число в ячейку строки row, столбца col.
                                           Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.

        table.n_rows() — вернуть число строк в таблице

        table.n_cols() — вернуть число столбцов в таблице

        table.delete_row(row) — удалить строку с номером row

        table.delete_col(col) — удалить колонку с номером col

        table.add_row(row) — добавить в таблицу новую строку с индексом row.
                             Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.

        table.add_col(col) — добавить в таблицу новую колонку с индексом col.
                             Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.
'''

import table as t

print("Пример 1:")
tab = t.Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

'''
Вывод:
0 10 0 0 0
0 0 20 0 0
0 0 0 30 0

0 10 0 0 0
0 0 0 0 0
0 0 20 0 0
0 0 0 30 0
'''


print("Пример 2:")
tab = t.Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
'''
Вывод:
0 0
0 0

10 20
30 40

None None None None
None 10 20 None
None 30 40 None
None None None None

None None None None None
None 0 0 0 None
None 10 0 20 None
None 30 0 40 None
None None None None None
'''


print("Пример  3:")
tab = t.Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

'''
Вывод

0

1000

None None None
None 1000 None
None None None

None None None None None
None 2000 0 3000 None
None 0 1000 0 None
None 4000 0 5000 None
None None None None None
'''