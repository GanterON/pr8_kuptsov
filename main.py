import random

a = 'abcdefghijklnopqrstuvwxyzADCDEFGHIJKLMNOPQRSTUVWXYZ'
b =''
for i in range(11):
    b += random.choice(a)
print(b)
