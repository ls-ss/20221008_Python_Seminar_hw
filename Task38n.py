''' Task38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
    (Сделать с использованием ф-ций: lambda, filter, map, zip, enumerate, list comprehension)
'''

txt = 'Программа Програбвмма абв удаляет абвудаляет из текста текстаабв \
словабв слова, котабабворое содержащие "aбв".'

# lambda, filter
print(' '.join(list(filter(lambda x: 'абв' not in x, txt.split()))))