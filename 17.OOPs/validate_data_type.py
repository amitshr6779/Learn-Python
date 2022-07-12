class Item:

    #constructor and  magic method defined
    def __init__(self, name: str, price: float, quantity=0):

        #run validation to recieved args
        assert price >= 1, f"price {price} is not greater or equals to zero!"
        assert quantity >= 1, f"quantity {quantity} is not greater or equals to zero!"

        #dynamicaly attributes assigned.
        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    #Creating a method
    def calculate_price(self):
        return self.price * self.quantity
#creating a instance item1
item1 = Item("chair", 500, 40)

#Assertion check
#item1 = Item("chair", -500, 40)

#Creating Another Instance
item2 = Item("Books", 80, 99)

#assertion check
#item2 = Item("Books", 80, -99)

#we can seprate attribute to any instance
#item1.has_student = True

print(item1.calculate_price())
print(item2.calculate_price())

