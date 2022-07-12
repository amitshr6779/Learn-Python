class Item:
    #Creating a method
    def calculate_price(self, x, y):
        return x * y
#creating a instance item1
item1 = Item()

#Creating attributes
item1.name = "Bag"
item1.price = 500
item1.quantity = 4

print(item1.calculate_price(item1.price, item1.quantity ))


#Creating Another Instance
item2 = Item()

item2.name = "Books"
item2.price = 99
item2.quantity = 6

print(item2.calculate_price(item2.price, item2.quantity ))
