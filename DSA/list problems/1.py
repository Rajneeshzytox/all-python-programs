# rotate a list

# input = [1,2,3,4,5] k = 2
# output = [4,5,1,2,3]

# test case = [1,2,3,4,5,6], k = 5
# output = [2,3,4,5,6,1]

# approach 1

a = [1,2,3,4,5,6]
len_a = len(a)
b = a.copy()

k = 5

for i in range(len_a):
    if(i+k > len_a - 1):
        b[i+k - len_a] = a[i]
    else:
        b[i+k] = a[i]

print(b)