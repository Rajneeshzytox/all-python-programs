# list:  1d to 2d and 2d to 1d

##########################
# 2D to 1D
a = [[1,2,3,4], [5,6]]

def to_one_D(a:list):
    temp = []
    for i in range(len(a)):
        temp += a[i]
    return temp
   
a = to_one_D(a)

print(a)


########################
# 2d to 1d

b = [1,2,3,4,5,6,7,8]
col = 6 # no of columns, remaining will add in next row

def to_2d(b:list, col:int):
    count = 0
    temp2 = []

    while(True):
       if(len(b) - count <= col):
           temp2.append(b[count:])
           break
       temp2.append([b[i + count] for i in range(col)])
       count+=col

    return temp2

b_nd = to_2d(b, col)

print(b_nd)