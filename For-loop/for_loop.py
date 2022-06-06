#Looping through all leter of string
for i in "k8 Academy":
    print(i) 

#Looping through Array
friends = ["Tom", "Jam", "Mac"]  
for i in friends:
    print(i)

#Use of range in for loop
for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

friends = ["Tom", "Jam", "Mac"]  
for i in range(len(friends)):
    print(friends[i])

#if else in for loop
for i in range(10):
    if i == 0:
        print("First Iteration")    
    else:
        print("Not First iteration")