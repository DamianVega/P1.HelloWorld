"""
Find sum of random numbers in a list
"""
#import random
#numlist = []
#for i in range(5):
    #num = random.randint(-100,100)
    #numlist.append(num)
#print(numlist)
#print(numlist[0]+numlist[1]+numlist[2]+numlist[3]+numlist[4])

import random
mylist = []
for i in range(20):
    number = random.randint(-100,100)
    mylist.append(number)
print(mylist)
sum = 0
for val in mylist:
    sum = sum+val
print("The sum of the list is :",sum)