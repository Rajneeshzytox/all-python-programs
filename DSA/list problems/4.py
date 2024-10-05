# list: merge two sorted list

# input = [1,3,5,7], [2,4,6]
# output = [1,2,3,4,5,6,7]


#--------------- giving output but not scalable or general
# upto = 13
# a  = [i for i in range(1,upto+1, 2)]
# b = [i for i in range(2, upto+1, 2)]
# c = []
# print(a,b)
# min_len = min(len(a), len(b))

# for i in range(min_len):
#     c.append(a[i])
#     c.append(b[i])

# c.extend(a[min_len:])
# c.extend(b[min_len:])

# print(c)

#-----------------------------------

list1, list2 = [1,2,3,4,9,14,78], [5,6,7,8,10,11,12,13,45]

def merge(list1, list2):
    temp_list1, temp_list2 = list1.copy(), list2.copy()
    output = []

    while(temp_list1 and temp_list2):
        a = temp_list1[0]
        b = temp_list2[0]
        if(a < b):
            output.append(temp_list1.pop(0))
            continue
        elif(a>b):
            output.append(temp_list2.pop(0))
            continue
        else:
            output.append(temp_list1.pop(0))
            output.append(temp_list2.pop(0))

    output.extend(temp_list1[:])
    output.extend(temp_list2[:])
    return output

print(merge(list1,list2))