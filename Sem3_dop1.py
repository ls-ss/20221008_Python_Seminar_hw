''' Sem3_dop1. Сгруппировать слова по "общим буквам".
    Пример:
        Input: ['ate', 'tea', 'tan', 'ate', 'nat', 'bat']
        Output: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
'''

list_s = ['ate', 'tea', 'tan', 'eat', 'nat', 'bat']
print('Список слов: ', list_s)
list_new = []
list_words = []

# Отсортируем и сохраним в новом списке все элементы list_s в алфавитном порядке,
# тем самым элементы каждой группы слов, будут иметь одни и те же обозначения.
for i in range(len(list_s)):
    list_words.append(''.join(sorted(list_s[i])))

# Используем множество, чтобы оставить только уникальные имена в list_words
words = set(list_words)

# Сравниваем уникальные имена со списком list_words. На тех индексах в list_words, где
# имена совпадают, группируем слова в списке list_s.
list_temp = []
for i in list(words):
    n = 0
    for j in list_words:
        if j == i:
            list_temp.append(list_s[n])
        n += 1
    list_new.append(list_temp)
    list_temp = []

print('Сгруппированые слова по "общим буквам":', list_new)
