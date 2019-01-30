"""
Create a list of numbers
-Ascending
-Descending
-Minimum
-Maximum
"""
mylist = [-2,-5,-1,-3,-4,0,4,2,5,1,3]
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
#print(mylist[-1])
minimum = min(mylist)
print(minimum)
#print(mylist[0])
maximum = max(mylist)
print(maximum)