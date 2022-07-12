class Item:
    #defining class attribute
    pay_rate = 0.8

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

#listing all class attributes
print(Item.__dict__)

#listing all instance attributes
print(item1.__dict__)

#accesing class attribute 
print(Item.pay_rate)

#Note: class attribute are accessible to  instance also
print(item1.pay_rate)