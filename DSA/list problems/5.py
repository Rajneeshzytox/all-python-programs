# list : move zeero to end
# input = [0, 1, 0,3,12]
# output = [1,3,12,0,0]

a = [0, 1, 0, 12, 14 , 14 , 35, 57, 0, 3, 0, 12, 0]


# -------------------------- approach 1
def move_zero(list1: list):
    zeros = []
    output = []
    for i in list1:
        if i == 0:
            zeros.append(i)
        else:
            output.append(i)
    output.extend(zeros)
    return output

print(move_zero(a))

# --------------------------- approach 2

no_of_zeros = a.count(0)
for i in range(no_of_zeros):
    a.remove(0)
    a.append(0)
print(a)
