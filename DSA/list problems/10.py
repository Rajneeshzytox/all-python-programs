# list: common element in 3 list
# input
a = [1,5,10,20,40,70,67]
b = [80,100,67,10]
c = [3,4,15,67,20,30,45,10 ,10]

# ------------------ using set intersection
print(list(set(a).intersection(set(b).intersection(set(c)))))


# ------------------ using in 
a_len = len(a)
b_len = len(b)
c_len = len(c)
min_arr = a if (a_len < b_len and a_len < c_len) else b if b_len < a_len and b_len < c_len else c
output = []

for i in min_arr:
    if( i in b and i in c and i in a):
        output.append(i)

print(output)