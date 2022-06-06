#How to define a function and call ?
def message():
    print("Hello User")

message()

#How to pass parameter to function ?
def message(name, age):
    print("Hello " + name + " , you are " + str(age) + "!") 

message("Tom", 26)
message("Jay", 30)

#How to use return statement in function ?
def cube(num):
    return num*num*num

result = cube(3)
print(result)