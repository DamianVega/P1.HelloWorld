'''
Find out how to solve the distance between any given coordinates
(x1-x2)+(y1-y2) then square root
'''
import math

x1=int(input("Enter a number for x1 : "))
y1=int(input("Enter a number for y1 : "))
x2=int(input("Enter a number for x2 : "))
y2=int(input("Enter a number for y2 : "))

distance=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print(distance)
