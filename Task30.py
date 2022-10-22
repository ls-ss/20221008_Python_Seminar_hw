''' Task30. Вычислить число π c заданной точностью d.

    Пример:
        при d = 0.001, π = 3.141. 10^(-1) ≤ d ≤ 10^(-10).
'''
precision = input('Введите желаемое значение точности числа π: ')
# Для вычисления числа π с заданной точностью используем ряд Нилаканта.
pi = 3
pi_alt = 2
x = 2
sign = 1
while abs(pi - pi_alt) > float(precision):
    pi_alt = pi
    pi += sign * 4 / (x * (x+1) * (x+2))
    x += 2
    sign = -sign

precision = len(str(precision).split('.')[1])
print(f'Число π с точностью до {precision} знаков равно: ', round(pi, precision))
