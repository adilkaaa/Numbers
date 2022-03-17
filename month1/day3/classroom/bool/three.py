a = int(input('n1: '))
b= int(input('n2: '))
c= int(input('n3: '))

if a>b>c:
    print(f'2) {a}, {c}')
elif b>a>c:
    print(f'2) {b}, {c}')
elif c>a>b:
    print(f'2) {c}, {b}')
elif a>c>b:
    print(f'2) {a}, {b}')
elif c>b>a:
    print(f'2) {c}, {a}')
elif b>c>a:
    print(f'2) {b}, {a}')
else:
    print('noooooo')


