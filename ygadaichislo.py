from random import randint
x = randint(1, 100)
p = 1
while True:
    z = int(input('Угадай число '))
    if z == x:
        print(f'eeeeeeeee nagiiiiiiiib, s {p} oy popytky!!!')
        g = str(input('poprobuesh eshe raz? '))
        if g != 'y':
            break
    if z != x:
        p += 1
        if z > x:
            print('zagadannoe chislo menshe')
        if z < x:
            print('zagadannoe chislo bolshe')
        if z == x:
            print('eeeeeeeee nagiiiiiiiib')


