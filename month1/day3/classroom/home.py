r1 = 'чон арык'
r2 = 'байтик'
r3 = 'ортосай'
f1 = 'кирпич'
f2 = 'пескоблок'
r = input('район: ')
f = input('материал: ')
u = int(input('участок: '))
price = int(input('цена: '))
if r==r1 or r==r2 or r==r3:
    if f == f1 and u <=4 and price<50000:
        print("Классный дом")
    elif f == f2 and u<=5 and price<45000:
        print('Классный дом')
    else:
        print('Не подходит такой дом мне.')
else:
    print('Не подходит такой дом мне.')
