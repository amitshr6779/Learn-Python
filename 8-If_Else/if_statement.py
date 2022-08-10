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

'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
n = int(input("Enter number between 1 to 100").strip())
if n in range(2,5) and n % 2 == 0:
    print("Not weired")
elif n in range(6,20) and n % 2 ==0:
    print("weird")
elif n > 20 and n % 2 ==0:
    print("Not weird")
else:
    print("Invalid number weird")   


#Alternative of above questions:
if __name__ == '__main__':
    n = int(input("Enter number"))
    if n % 2 != 0 or n > 5 and n < 21 :
        print("Weird")
    else: 
        print("Not Weird")