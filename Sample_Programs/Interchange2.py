def interchange(l):
    first = l.pop(0)
    last = l.pop(-1)
    l.append(first)
    l.insert(0, last)
    return l

list = [1,2,3,4,5]
print(list)

new_list = interchange(list)
print(new_list)