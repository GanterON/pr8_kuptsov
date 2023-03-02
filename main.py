import random

a = 'abcdefghijklnopqrstuvwxyzADCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
b =''
for i in range(11):
    b += random.choice(a)
print(b)
