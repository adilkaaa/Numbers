w = ['python','java','javascript']
l = input('Язык программирования: ')
age = int(input('Age: '))
e = int(input('Опыт: '))
s = int(input('зарплата: '))

if l in w and 18<=age<=65 and e >=3 and s<=60000:
        print('Вы проходите на работу')
else:
    print('Вы нам не подходите!!!')
