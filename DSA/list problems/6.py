# intersection of 2 list

a = [1,2,3,4]
b = [3,4]


# ----------------- approach 1 : set method
print(list(set(a).intersection(set(b))))

# ----------------- appoach 2
def intersection_list(a,b):
    output = []
    for i in a:
        if i in b:
            output.append(i)
    return output

print(intersection_list(a,b))


