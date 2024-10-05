# print(dir(tuple))
# Methods
#  'count', 'index'

# a = (2,3,4) #same to  a = 2,3,4
# a = 2,3,4
# print(a)
# print(type(a))

# (x, y, z) = (2,3,4)
# print(f"x is {x}, y is {y}, z is {z}")

# swapping
# x, y = 5, 6
# print(f"x is {x}, y is {y}")
# x, y = y, x
# print(f"x is {x}, y is {y}")


# a = 2,3,4
# print( 3 in a) # true
# print( 5 in a) # false

# a = (1,2,3,4)
# b = [i for i in a] # tuple is itrable
# print(b)

######## count #########
# a = (5,5,5,5,5,5,7,7,7,7,8,8,8)
# print(a.count(7)) # 4
# print(a.count(5)) # 6
# print(a.count(8)) # 3


######## changing the value of the list inside tuple #########
# a = ([2,3,4], 3, 'hello', 5.5, 0b101) 
# a[0][0] = 5 # changes the value of the item inside tuple
# print(a) 



######## index #########
a = (67,65,68, 66, 65, 65)
# print(a.index(79))  ## !!!!!!!!!!!!!!!  ===>> value error