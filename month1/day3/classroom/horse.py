x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
if x1+2 == x2 and (y1+1==y2 or y1-1 ==y2):
    print(True)
elif x1-2==x2 and(y1-1==y2 or y1+1==y2):
    print(True)
elif x1+1==x2 and (y1+2==y2 or y1-2==y2):
    print(True)
elif x1-1 ==x2 and (y1+2==y2 or y1-2==y2):
    print(True)
else:
    print(False)

