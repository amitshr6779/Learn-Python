#Store items as key:value pair in Dictionary.
from unittest import mock


Month_index = {
    1: "january",
    2: "February",
    3: "March",
    4: "April"
}
print(Month_index)

#Access Spefic value.
print(Month_index[2])
print(Month_index.get(4))

#Add message for undefined key.
print(Month_index.get(3, "Key:value not defined"))