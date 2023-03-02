import random

a = 'abcdefghijklnopqrstuvwxyz'
b =''
for i in range(11):
    b += random.choice(a)
print(b)
