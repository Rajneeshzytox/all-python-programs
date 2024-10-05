# list: all pairs of giving sum || sum upto target

# input = [2,4,3,5,7,8,9], target = 7
# output = [(2,5), (3,4)]
# cant add to self (index) like (2,2) both at index 0, if duplicates present then yes
# 


#--------------------------------------
# input = [2,4,3,5,7,8,9]
# target = 7
# output = []
# for i in range(len(input)):
#     for j in range(len(input)):
#         if( i == j):
#             continue
#         elif(input[i] + input[j] == target):
#             output.append((input[i], input[j]))

# print(output)
#-------------------------------------
# input = [2,4,3,5,7,8,9]
# len_input = len(input)
# target = 7
# output = []
# for i in range(len_input):
#     for j in range(i+1, len_input):
#         if(input[i] + input[j] == target):
#             output.append((input[i], input[j]))

# print(output)
#--------------------------------------

target = 7
input = [2,4,3,5,7,8,9,10,9,1,2,3,4,6,64,54,34,42,24,454,65,6,57,6,74,53,43,43,43,4]
# sinput = input.sort()

# new_input = sorted([i for i in input if i < target]) 
# print(new_input) 

## >>> here without set conversion we are getting output as:
## >>> [(1, 7), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (3, 5), (3, 5), (4, 4), (4, 4), (4, 4)]

input = list(set(input))
new_input = sorted([i for i in input if i < target])
print(new_input)


len_input = len(new_input)
output = []

for i in range(len_input):
    for j in range(i+1, len_input):
        if(new_input[i] + new_input[j] > target):
            break
        elif(new_input[i] + new_input[j] == target):
            output.append((new_input[i], new_input[j]))
        

print(output)

