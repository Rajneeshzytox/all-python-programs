# list: find the median
# median = middle element
# if odd -> n/2
# if even -> (n/2 + n/2+1)/2

list1 = [2,4,5,3,1,6,8,7]
# 1,2,3,4,5,6,7,8,9

#------------------------- using methods sort(), len()

list1.sort()
n = len(list1)

if(n&1 == 0):
    mid = (n//2 + (n//2+1))//2
else:
    mid = (n//2)

print(list1[mid])






