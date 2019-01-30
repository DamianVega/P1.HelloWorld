'''
Assignment 2
'''
import random #import a library to create random numbers
numlist = []
for i in range(20):
    num = random.randint(-100,100)
    numlist.append(num)
print(numlist)
numlist.sort()
print(numlist)
numlist.reverse()
print(numlist)
minimum = min(numlist)
print(minimum)
maximum = max(numlist)
print(maximum)