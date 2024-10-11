# list: pair of difference 

a = [1,2,3,4,5,6]
target = 3
# (3,1) (4,2) (5,3) (6,4)

# ------------------ straight loop

output = []
for i in a:
    for j in a:
        if(i == j):
            continue
        if(i-j == target):
            output.append((i,j))
print(output)

# ------------------- single loop

for i in a:
    if(a.count(i - target) >=1):
        print((i, i-target))

