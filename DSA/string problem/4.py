# string: remove space from string

str1 = 'h e l l o'


# ------------ split() ------------
a = str1.split()
a = ''.join(a)
print(a)


# -------------- array remove(' ') ------------
b = list(str1)
while(b.count(' ')):
    b.remove(' ')

print(''.join(b))


# ------------- loop ------------
print(''.join([i for i in str1 if i!=' ']))


# ------------- simple loop  ------------
d = ''
for i in str1:
    if(i == ' '):
        continue
    d += i
print(d)