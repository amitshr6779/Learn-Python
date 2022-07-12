freinds = ["tom", "mac", "john", "jay", "john", "henry"]
lucky = [2, 4, 6, 8, 10]

print(freinds)

print(freinds[3])

print(freinds[2:])

print(freinds[2:4])

print(freinds[-1])

#modify value in List
freinds[1] = "Mike"
print(freinds)

#concetenate one list to another
#freinds.extend(lucky)
#print(freinds)

#add more value in the end of existing list 
freinds.append("Rahul")
print(freinds)

#add value  in middle of list
freinds.insert(1, "Modi")
print(freinds)

#find out index of a item in list
print(freinds.index("Rahul"))

#count items in list
print(freinds.count("john"))

#sort list
freinds.sort()
lucky.sort()
print(freinds)
print(lucky)

#reverse list
freinds.reverse()
print(freinds)

#copy list to new list
old_friends = freinds.copy()
print(old_friends)

#to clear list item in list
lucky.pop()
print(lucky)

#to clear list
lucky.clear()
print(lucky)



