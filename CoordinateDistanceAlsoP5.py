'''
Finding the distance between a point and (0,0) in 3d
'''
def distance3d(x1,y1,z1,x2,y2,z2):
    d=math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return d