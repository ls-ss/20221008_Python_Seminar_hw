''' Task 7.
    Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    ¬ (not),
    ⋁ (or),
    ⋀ (and)
'''
print('| X | Y | Z | F1 | F2 | STATUS |')
print('--------------------------------')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            f1 = not(x or y or z)
            f2 = (not x) and (not y) and (not z)
            print(f'| {int(x)} | {int(y)} | {int(z)} | {int(f1)}  | {int(f2)}  |   {"OK" if f1 == f2 else "no"}   |')
