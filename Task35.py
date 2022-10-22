''' Task35. Даны два файла, в каждом из которых находится запись многочлена.
    Задача - сформировать файл, содержащий сумму многочленов.
'''

# Заданные многочлены
polynom1 = '-6*x^6 - 4*x^4 - 2*x^2 - 1'
polynom2 = '8*x^4 + 3*x^3 + 2*x^2 + 5*x + 2'

# Записываем заданные многочлены в файлы
with open('task35_polynom1.txt', 'w', encoding="utf-8") as f:
    f.write(polynom1)
with open('task35_polynom2.txt', 'w', encoding="utf-8") as f:
    f.write(polynom2)

# Читаем с файлов многочлены
with open('task35_polynom1.txt', 'r') as f:
    polynom_1 = f.readline()
with open('task35_polynom2.txt', 'r') as f:
    polynom_2 = f.readline()
print('Первый многочлен: ', polynom_1)
print('Второй многочлен: ', polynom_2)

# Избавляемся от пробелов. Разбиваем строку на списки строк по разделителю '+' или '-'
list_polynom1 = polynom_1.replace('- ', ' -').replace('+', ' ').split()
list_polynom2 = polynom_2.replace('- ', ' -').replace('+', ' ').split()
#print(list_polynom1, list_polynom2)

dict_polynom1 = {}
for st in list_polynom1:
    if not(st.count('x')):
        dict_polynom1[0] = int(st)
    else:
        st = st.replace('*x^', ' ')
        st = st.replace('x^', '1 ')
        st = st.replace('*x', ' 1')
        st = st.replace('x', '1 1')
        st = st.split()
        dict_polynom1[int(st[-1])] = int(st[0])

dict_polynom2 = {}
for st in list_polynom2:
    if not(st.count('x')):
        dict_polynom2[0] = int(st)
    else:
        st = st.replace('*x^', ' ')
        st = st.replace('x^', '1 ')
        st = st.replace('*x', ' 1')
        st = st.replace('x', '1 1')
        st = st.split()
        dict_polynom2[int(st[-1])] = int(st[0])
#print(dict_polynom1, dict_polynom2)

key_polynom1 = [*dict_polynom1.keys()]
key_polynom2 = [*dict_polynom2.keys()]
#print(key_polynom1, key_polynom2)

# Создаем новый словарь, в котором объединяем два предыдущих словаря, сложив значения по одинаковым ключам
dict_polynom = {}
for key in key_polynom1:
    if dict_polynom2.get(key) is not(None):
        if dict_polynom1[key] + dict_polynom2[key]:
            dict_polynom[key] = dict_polynom1[key] + dict_polynom2[key]
        del dict_polynom2[key]
    else:
        dict_polynom[key] = dict_polynom1[key]
#print(dict_polynom, dict_polynom2)
# Добавляем оставшиеся значения с уникальными ключами из словаря dict_polynom2
for key in dict_polynom2:
    dict_polynom[key] = dict_polynom2[key]
#print(dict_polynom)

# Организуем вывод нового словаря в виде многочлена
key_polynom = sorted(dict_polynom)[::-1] # Сортируем словарь по ключам
#print(key_polynom)

new_polynom = ''
for i in key_polynom:
    if (dict_polynom[i] < 0) and (i != key_polynom[0]):
        new_polynom += ' - '
    elif i < key_polynom[0]:
        new_polynom += ' + '

    if i == 0:
        new_polynom += str(dict_polynom[0])
    else:
        if abs(dict_polynom[i]) != 1:
            new_polynom += str(dict_polynom[i]) + '*'

        new_polynom += 'x'
        if i != 1:
            new_polynom += '^' + str(i)

print('Сумма многочленов: ', new_polynom)

# Создаем файл и записываем туда созданный многочлен
with open('task35_polynom.txt', mode='w', encoding="utf-8") as f:
    f.write(new_polynom)
