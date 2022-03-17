m = int(input('оперативная память: '))
disk = int(input('ssd: '))
hdd = int(input('hdd: '))
price = int(input('price: '))
new = True
if 4<=m<=8:
    if  disk>=256 or hdd >1:
        if price <=1000 and new == True:
            print('great laptop')
else:
    print('no need that laptop')
