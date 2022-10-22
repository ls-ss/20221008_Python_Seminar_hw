''' Task31. Задайте натуральное число N. Напишите программу,
    которая составит список простых множителей числа N.
'''

def Factor(num):
    list_prime = []
    num_prime = 2
    while num_prime**2 <= num:
        if not(num % num_prime):
            list_prime.append(num_prime)
            num //= num_prime
        else:
            num_prime += 1
    if num > 1:
        list_prime.append(num)
    return list_prime

print(Factor(int(input('Введите целое число: '))))
