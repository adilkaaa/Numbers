exit = False
l =[]
while not exit:
    print('''
Выберите действие:
1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход''')
    q = int(input('Выберите действие: '))
    if q == 1:
        c = input('Введите название города: ')
        if c not in l:
            l.append(c)
            print('Город добавлен успешно!')
            print()
        else:
            print('Такой город уже существует.')
    elif q == 2:
        print(l)
        print()
    elif q == 3:
        old = input('Текущий город: ')
        new = input('Новый город: ')
        if new in l:
            print('Такой город уже существует!')
        elif old not in l:
            print('Некоректное название города!')
        else:
            i = l.index(old)
            l[i] = new
            print('Город заменен!')
            print()
    elif q == 4:
        r = input('Введите название города: ')
        if r not in l:
            print('Некорректное название!')
        else:
            l.remove(r)
            print('Город удален!')
    elif q ==5:
        print('Goodbye!!!')
        exit = True
    else:
        print('Введите цифру правильно!')
    
    