# String: Reverse a string

str1 = 'hello world of python'

# -------------------- slicing 
print(str1[::-1])

# -------------------- list reverse
a = list(str1)
a.reverse()
a = ''.join(a)
print(a)

# -------------------- function for loop
c =''
for i in range( len(str1) - 1, -1, -1):
    c += str1[i]

print(c)
