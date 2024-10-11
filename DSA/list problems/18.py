# list: frequency of each element
# already done in 7.py


a = [1,2,3,4,5,6,6,7,7,7,8,6,5,4,4,3,3,3,2,2,1,3,3,4,5,6,7,7,9]

# ------------------ using set

output = {}

new_a = set(a)
for i in new_a:
    output.setdefault(i, a.count(i))

print(output)

