w = input('word: ')
d = w.lower()
i = d[::-1]
if d == i:
    print(d, 'is palindrome')
else:
    print('Not palindrome')
