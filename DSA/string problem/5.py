# string: convert to uppercase without in built methods

str1 = 'hello ^ & [ world ] ``` of \\ python```'

# ---------------------- A = 65, a = 97, Z = 65+25= 90, z = 97+25= 122
# # 97-65 = 32

def returnUpperChar(s:str):
    ascii_of_str = ord(s)
    if(ascii_of_str >= 97 and ascii_of_str <= 122):
        ascii_of_str -= 32
        return chr(ascii_of_str)
    return False


output = ''
for i in str1:
    temp_char = returnUpperChar(i)
    if temp_char:
        output += temp_char
    else:
        output += i

print(output)

