#Python | Ways to check if element exists in list
def check(l,n):
    for i in l:
        if n == i:
            return "yes"
    return "no"

num = int(input("Enter the number u want to check in list: "))
list = [12, 22, 32, 42, 52]
output = check(list,num)
print("Number Present: " + str(output))