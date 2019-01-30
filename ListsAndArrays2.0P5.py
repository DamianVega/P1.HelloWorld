"""
Traversing Lists
For Loop, Membership, Enumerate(list) - Function
"""
mylist = ["Apple", "Pear", "Banana","Orange"]
# Membership
if "Watermelon" in mylist:
    print("Yes")
else :
    print("No")
# Use Membership to print every element in the list
for var in mylist:
    print(var)
# Print every element in the list using their indexes
for index in range(len(mylist)):
    print(mylist[index])
# Using a numerate of the list/function
for (index, value) in enumerate(mylist):
    print(index, value)