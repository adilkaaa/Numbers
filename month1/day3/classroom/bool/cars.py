cars = ['лексус', 'тойота']
colors = ['белый','серый']
r = 'левый'

year = int(input('год: '))
car = input('марка: ')
p = int(input('пробег: '))
color = input('цвет: ')
owner = int(input('сколько хозяинов: '))
rul = input('руль: ')
price = int(input('цена: '))
if car in cars and color in colors and year>=2004 and owner<=2 and rul ==r:
    if price <=10000 and p==150000:
        print('Классная машина!')
    elif price<=8000 and p==200000:
        print('Классная машина!!!')
    else:
        print('NO THANKS(')
else:
    print('NO THANKS(')