# string: palindrom check

str1 = 'NITIN'

# ----------------- slicing
print(f'{str1} is palindrom') if str1 == str1[::-1] else print(f'{str1} is not palindrom')

# ----------------- LIST REVERSE
a = list(str1)
a.reverse()
a = ''.join(a)

print(f'{str1} is palindrom') if str1 == a else print(f'{str1} is not palindrom')


# ------------------ loop
len_a = len(a)
isPalindrom = False
for i in range(len_a):
    if(a[i] != a[len_a -1 -i]):
        isPalindrom = False
        break
else: 
    isPalindrom = True

print(f'{str1} is palindrom') if isPalindrom else print(f'{str1} is not palindrom')
    

# ------------------ Recursion
def isPalindromFun(s:str):
    if(len(s) == 0 or len(s) == 1):
        return True
    elif(s[0] != s[-1]):
        return False
    return isPalindromFun(s[1:-1])


print(f'{str1} is palindrom') if isPalindromFun(str1) else print(f'{str1} is not palindrom')
