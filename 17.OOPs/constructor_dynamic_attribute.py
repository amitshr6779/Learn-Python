class Item:

    #constructor and  magic method defined
    def __init__(self, name, price, quantity=0):

        #dynamicaly attributes assigned.
        self.name = name
        self.price = price
        self.quantity = quantity

    #Creating a method
    def calculate_price(self):
        return self.price * self.quantity
#creating a instance item1
item1 = Item("chair", 500, 40)

#Creating Another Instance
item2 = Item("Books", 80, 99)

#we can seprate attribute to any instance
#item1.has_student = True

print(item1.name)
print(item1.price)
print(item1.quantity)

print(item2.name)
print(item2.price)
print(item2.quantity)

print(item1.calculate_price())
print(item2.calculate_price())

