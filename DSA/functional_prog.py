# ____________________________________________________________________
# filter 
# print(help(filter))

# def check(x):
#     if(x%2 == 0 and x%4==0):
#         return True
#     return False

# list1 = [i for i in range(2,51)]

# print(list(filter(None, list1))) 
# ## return only true element form iterable

# print(list(filter(check, list1)))
# ____________________________________________________________________

## Map ##
# list1 = [i for i in range(11)]
# def double(x):
#     return x*2

# print(list(map(double, list1)))

# def add(x,y):
#     return x+y

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# print(list(map(add, list1, list2)))

# ____________________________________________________________________

## reduce
# import functools as ft
# def add(x,y):
#     print(x+y, end=" ")
#     return x+y
# list1 = [1,2,3,4]
# print(ft.reduce(add, list1))



# ____________________________________________________________________