#Use of if-else statement.
is_male = True
if is_male:
    print("You are Male")
else:
    print("You are not male")    

#use of OR operator.
is_male = True
is_tall = True
if is_male or is_tall:
    print("You are Male and tall")
else:
    print("You are not male a nor tall")

#use of AND operator.
is_male = True
is_tall = False
if is_male or is_tall:
    print("You are Male and tall")
else:
    print("You are not male or not  tall")

#use of elif
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are Male and tall")
elif is_male  and  not(is_tall):
    print("You are male but not tall")
elif not(is_male) and is_tall:
    print("You are not male but tall")    
else:
    print("You are not male, nor tall")

#Use of if else with comaprison opeartor and functions.
def max_value(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_value(2, 8, 19))