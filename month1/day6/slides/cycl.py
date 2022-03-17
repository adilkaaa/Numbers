#1

languages = ['go','java','php','python','javascript','ruby']
lang1 = 'Rust'
for l in languages:
    if l == lang1:
        print('this language in list')

#2
l = []
i = 0
while i<len(languages):
    if languages[i]!='php':
        l.append(languages[i])
        i+=1
    else:
        break
print(l)


#3
n = 7
for i in range(5):
    n*=n
    print(n)

#4
for i in range(len(languages)):
    print(i,languages[i])

#5
n = 0
for i in range(1,20):
    if i <= 10:
        n = i
    else:
        n-=1
    print(n,end=",")

#6
names = ['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']
for i in range(0,len(names),2):
    print(names[i])
print()

#7
for i in range(1,13,2):
    print(names[i])

#8
while True:
    n = int(input('number: '))
    if n>99 and n<1000:
        print('Это число трехзначное')
    if n>0 and n%2==0:
        print('Это число положительное и четное')
    if n%31==0:
        print('Это число делится на 31 без остатка')
    if (n>100 and n%17==0) or (n>150 and n== 13**2):
        print(n)
    if n==0:
        break
#9
l1 = []
l2 = []
n=0
for i in range(-100,100):
    if i%13 == 0 and i%2==0:
        # print(i**2)
        l1.append(i**2)
    n+=1
    if n ==7:
        if i%2!=0:
            print(i)
            l2.append(i)
        n = 0
print(f'for 1st condition: {len(l1)}')
print(f'for 2nd condition: {len(l2)}')


