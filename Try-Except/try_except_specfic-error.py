#use specfic error catch.
try:
    num1 = int(input("Enter a number: "))
    result = 10/0
    print(result)

#except ZeroDivisionError:
except ZeroDivisionError as err:
    #print("oops ! Trying to divide bt zero")
     print(err)

#except ValueError:
except ValueError as wrong:
    #print("Inavlid Input")
    print(wrong)