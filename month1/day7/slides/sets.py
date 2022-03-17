#0
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

#1
s1 = {1,2,3}
s2 = {4,5,6}
s3 = {7,8,9}
s4 =set()
s4.update(s1)
s4.update(s2)
s4.update(s3)
print(s4)

#2
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}

print(farm_2.difference(farm_1))

#3
s = {1,2,3,4,5}
s.add(6)
s.pop()
print(s)

#4
d = set()
for i in range(10):
    a  = int(input('num: '))
    d.add(a)
d = frozenset(d)
print(d)


#5
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
f3 = farm_1.union(farm_2)
print(f3)

f4 = farm_1.difference(farm_2)
print(f4)