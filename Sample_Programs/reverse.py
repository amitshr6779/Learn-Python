#Python | Reversing a List
from copy import copy


def rev(l):
    new_list = copy(l)
    length = len(l)
    for i in l:
        length = length - 1
        new_list[length] = i
    return new_list

        

list = [1,2,3,4,5]
print(rev(list))