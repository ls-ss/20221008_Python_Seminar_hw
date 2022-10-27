''' Task42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. '''

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:   # Если предыдущий и текущий символы не совпадает
            if prev_char:   # Добавляем число и символ в нашу кодировку
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1  # Увеличиваем счетчик если символы одинаковы
    else:               # Завершить кодировку
        encoding += str(count) + prev_char
        return encoding

print(rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'))
