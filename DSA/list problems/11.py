# list: remove odd int from lis///t

list1 = [1,2,3,4,5,6,7,8]

# --------------------- bitwise list comprehension

print([i for i in list1 if i&1!=1])

# --------------------- loops

for i in list1:
    if i&1 != 1:
        print(i)

