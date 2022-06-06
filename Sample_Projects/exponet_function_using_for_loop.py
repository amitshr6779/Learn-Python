def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = result * base_num
    return result 

print(raise_to_power(2, 4))