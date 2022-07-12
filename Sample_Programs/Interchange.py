#Python program to interchange first and last elements in a list

def iterchange(l):
    temp = l[0]
    length = len(l)
    l[0] = l[length -1]
    l[length -1] = temp
    
    return l


list = [1,2,3,4,5]
new_list = iterchange(list)
print("Interchanged list is")
print(new_list)


        