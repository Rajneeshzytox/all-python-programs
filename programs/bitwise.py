# bitwise questions
# perator = & | ^ >> <<

# count the no of 1's
n = 10
count = 0
while (n > 0):
    if n&1 == 1:
        count += 1
    if(n == 0):
        break
    n = n>>1

print(count)

# a = (str(bin(7))[2:]).count('1')
# print(int(a))



