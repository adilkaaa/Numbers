# 1
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = {'Coca-cola':90,
'Sprite':70,
'Fanta':80}
print(menu['drinks'])
print()

# 2
d = {}
for i in range(3):
    name = input('name: ')
    password = input('password: ')
    d[name]=password
print(d)
print()

# 3
d2 = {
    'Adil':'Программист',
    'Beks': 'Инженер',
    'Adelina': 'Маркетолог',
    'Damir': 'Врач',
    'Nastya':'Бухгалтер'
}
for k,v in d2.items():
    print(f'Здравствуйте {k}. Прекрасная профессия {v}')
print()

# 4
menu['besh_barmak'] = 130
menu['lagman'] = 135
del menu['borsh']
for k,v in menu.items():
    print(k,v)
print()

# 5
c = {}
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
i = 1
for country in sorted(frozenset(countries)):
    c[i]= country
    i+=1
print(c)



