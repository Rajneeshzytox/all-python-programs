# remove duplicates from list
# -----------------------------------------------------------------------
# Method 1
a = [1,1,2,2,3,3,4,5,6,6,5,4,3,4,5,2,3,1]
b = []
def check(x):
    if x in b:
        return
    b.append(x)
    return

list(filter(check, a))

print("a : ", a)
print("b : ", b)

# -----------------------------------------------------------------------

