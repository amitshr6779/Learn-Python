operator = input("Which operation you want to perform ")
num1 = float(input("Enter First number "))
num2 = float(input("Enter Second number "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)    
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")


