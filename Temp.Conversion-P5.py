'''
Convert from F to C, and from C to F
'''
degree = input("Enter c for Celsius, or f for Fahrenheit:")
temp = int(input("Enter the temperature's value:"))
if degree == 'f':
    C = (temp-32)*5/9
    print("The converted temperature in Celsius is :", round(C))
elif degree == 'c':
    F = temp*9/5+32
    print("The converted temperature in Fahrenheit is :", round(F))
else:
    print("The temperature you inputted does not exist :", degree)
exit()