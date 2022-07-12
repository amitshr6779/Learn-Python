class Item:
    all = []
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

        #Action to execute, appending all attribute to list :all
        Item.all.append(self)

    #Creating a method
    def calculate_price(self):
        return self.price * self.quantity
    # magic metrhod to represent object in human fiendly
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"



#creating a instance item1
item1 = Item("chair", 500, 40)
item2 = Item("Books", 80, 99)
item3 = Item("pen", 10, 40)

print(Item.all)

for instance in Item.all:
    print(instance.name, instance.price)



