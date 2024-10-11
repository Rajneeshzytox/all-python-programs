# list: mode (most repeted value)

a = [1,2,3,2,2,11,1,1,1,1,11,1,2,3,3,4,44,4,5,6,6,7,7,8,8,8,]

new_a = list(set(a))
mode_majority = -1
mode = -1
output = {}
count = 0
for i in new_a:
    count = a.count(i)
    output.setdefault(i, count)
    if(count > mode_majority):
        mode_majority = count
        mode = i

# print(output)

print(f"'{mode}' is mode as it repeats {mode_majority} times")