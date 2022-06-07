from chef import Chef
from special_chef import  Special_chef

myChef = Chef()
print(myChef.veg_dish())

spChef =  Special_chef()
print(spChef.veg_dish())
print(spChef.non_veg_dish())
print(spChef.extra_dish())