'''
Put here all the definitions for specific formulas
'''
import math
def fibonacci_sequence(n):
    x=1
    y=1
    count=1
    while count <= n:
        print('The next Fibonacci number is',x+y)
        temp=x
        x=y
        y=y+temp
        count=count+1
def swap(a,b):
    temp=a
    a=b
    b=temp
    return print(a,b)

def distance2d(x1,y1,x2,y2):
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return d

def distance3d(x1,y1,z1,x2,y2,z2):
    d=math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return d

def convert_list_to_word(alist):
    new_word = ''
    n = len(alist)
    for index in range(n):
        new_word = new_word + alist[index]
    return new_word

def eliminate_repeats(oldlist):
    newlist = []
    for element in oldlist:
        if element not in newlist:
            newlist.append(element)
    return newlist

def translate(text1,dict1):
    list_text = text1.split()
    new_text = []
    for word in list_text:
        translation = dict1.get(word)
        new_text.append(translation if translation else word)
    return ' '.join(new_text)
