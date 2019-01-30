'''
1) Swap 2 variables
2) Fibonacci Sequence
'''
# a=10
# b=5
# print('The value of a =',a,"and the value of b =",b)
# # Create a temporary var to store a
# temp=a
# a=b # Assign variable b to variable a
# b=temp # Assign the temp variable (former value of a)
# print('The value of a =',a,"and the value of b =",b)

# While loop
# x=1
# while x<10:
#     print(x,end=' ')
#     x=x+1

# cont='c'
# while cont=='c':
#     print('The World is Beautiful.')
#     cont=input('Do you want to keep living? Press c, otherwise, press any key.')

# Fibonacci Sequence
x=1
y=1
cont='c'
while cont == 'c':
    print('The next Fibonacci number is',x+y)
    temp=x
    x=y
    y=y+temp
    cont=input('Press c for the next Fibonacci number. If not press any key.')