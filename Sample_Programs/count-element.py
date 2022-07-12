def count_num(l,n):
    c = 0
    for i in l:
        if i == n:
            c += 1
    return c

num = int(input("enter a number to search"))
list = [2,3,4,5,7,8,9,2,3,4,5,6]
print(count_num(list,num))