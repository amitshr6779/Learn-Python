#Python program to swap two elements in a list
def swap(l,p1,p2):
    temp = l[p1]
    l[p1] = l[p2]
    l[p2] = temp
    return l

list = [2,4,6,8,10]
pos1 = 1
pos2 = 3
print(swap(list, pos1, pos2))