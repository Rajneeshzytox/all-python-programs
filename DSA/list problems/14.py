# list : concate two list

list_main_1 = [1,2,3,4,5]
list_main_2 = [6,7,8,9,0]

# ------------------- extend()
list1  =list_main_1.copy()
list2  =list_main_2.copy()

list1.extend(list2)
print(list1)


#------------------- add operaor
print(list_main_1 + list_main_2)


# ------------------ indexing
output = []

output += list_main_1[:]
output += list_main_2[:]

print(output)

# ----------------- loop

output = []

for i in list_main_1:
    output.append(i)
for i in list_main_2:
    output.append(i)

print(output)
