from operator import length_hint
import random
password = ''
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_~123456789'
length = int(input("Enter how much lenghth  of password you want! "))
for i in range(length):
    password = password+random.choice(char)
print(password)