s = 0
i = 0
while s<1000:
    print(i)
    i+=1
    if s<0:
        break
    s+=i

while True:
    a = int(input('Введите число: '))
    if a>100:
        print('Вы ввели число больше 100')
        break
    
