o = int(input('oclad: '))
calDay = int(input('calendar days: '))
workDay = int(input('work days: '))
p = int(input('premii: '))
nalog = 13
u = int(input('shtraf: '))
salary = (o/calDay * workDay + p)*((100-nalog)/100)-u
print(f'SALARY - {salary}')

