"""
Operations with Lists
Keywords : addition(coacatenate), slices, deleting(removing) elements
"""
alist = ["a","b","c","d","e"]
blist = ["w","x","y","z"]
# Adding/Multiplying
print(alist+blist)
print(alist*4)
# Slicing
print(alist[1:3])
print(alist[:3])
print(alist[0:])
print(alist[:1])
# Squeezing
alist[2:2] = blist[0:]
print(alist)
alist[4:7] = []
print(alist)
del alist[0]
print(alist)
alist[0:0] = ["a"]
print(alist)
del alist[:2]
print(alist)