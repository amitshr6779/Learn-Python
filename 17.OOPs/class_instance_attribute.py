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

    #accessing pay_rate from class label (Item.pay_rate) and instance label (self.label)
    def discount_price(self):
        self.price = self.price * self.pay_rate 

#creating a instance item1
item1 = Item("chair", 500, 40)
item1.discount_price()
print(item1.price)

item2 = Item("chair", 500, 40)
#assing pay_rate at instance label
item2.pay_rate = 0.7
item2.discount_price()
print(item2.price)
