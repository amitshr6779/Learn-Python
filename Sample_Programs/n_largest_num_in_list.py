#Python program to find N largest elements from a list
list = [10,8,17,4,19,80]
list.sort()
n = int(input("Enter the how much largest number you want to fetch from list: "))
print(list[-n:])