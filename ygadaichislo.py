x = 26
p = 1
z = int(input('Угадай число '))
if z == x:
    print('eeeeeeeee nagiiiiiiiib, s 1oy popytky!!!')
while z != x:
    p += 1
    if z > x:
        print('zagadannoe chislo menshe')
        z = int(input('poprobuy eshe raz '))
    if z < x:
        print('zagadannoe chislo bolshe')
        z = int(input('poprobuy eshe raz '))
    if z == x:
        print('eeeeeeeee nagiiiiiiiib')
        print(f'ty spravylsya so {p} popitky!')
