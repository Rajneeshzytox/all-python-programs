# list: smallest positive missing numb

a = [6,4,7,2,9,3,8,1,0]
# 5

# ------------------- loop
for i in range(max(a)):
    if i not in a:
        print(i)
        break

# ------------------- without not in
a.sort()
for i in range(max(a)):
    if(a[i] + 1 != a[i+1]):
        print(a[i] +1)
        break
