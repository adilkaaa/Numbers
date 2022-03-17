a = input('text: ')

if a.count('.')==1:
    b = a.index('.')+1
    print('Расширение файла:',a[b:])
else:
    print('Расширение не найдено')


