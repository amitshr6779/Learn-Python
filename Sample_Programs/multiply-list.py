def mul(l):
    product = 1
    for i in l:
        product = i * product
    return product        
list = [12,2,10]
print(mul(list))