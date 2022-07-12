list = []
num = int(input("Enter tolal number of elemets in list"))
for i in range(0, num):
    ele = input("Enter your element")
    list.append(ele)
print(min(list))    