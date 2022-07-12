import csv
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
    
    @classmethod
    def instanciate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                qunatity = int(item.get('quantity'))
            )
            #print(item)


Item.instanciate_from_csv()
