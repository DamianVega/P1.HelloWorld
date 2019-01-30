'''
Finding tghe mean, median, mode of a random list
'''
import random #import a library to create random numbers
numlist = []
for i in range(10):
    num = random.randint(0,5)
    numlist.append(num)
print(numlist)
sum = 0
for val in numlist:
    sum = sum+val
mean = sum/10
print("The Mean of the list is :",mean)