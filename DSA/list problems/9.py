# list: remove a number from a list completely

a  = [1,1,3,2,3,2]
num = 3
#---------------------- approach 1
def remove_num1(a, num):
    output = []
    for i in a:
        if i != num:
            output.append(i)
    return output

print(remove_num1(a, num))

#---------------------- approach 2

def remove_num2(a:list, num:int):
    while True:
        try:
            a.remove(num)
        except:
            break
    return a
print(remove_num2(a,num))

#---------------------- approach 3

def remove_num3(a:list, num:int):
    while True:
        try:
            a.pop(a.index(num))
        except:
            break 
    return a

print(remove_num3(a, num))