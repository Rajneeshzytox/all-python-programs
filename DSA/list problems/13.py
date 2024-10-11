# list: Kth largest element

list1 = [8,9,8,7,6,9,7,6,5,4,2,3,1,5,6,7,9,8,7,6,5,4,3,2,1]
k = 1
# -------------------------- using methods and set

tmp_list = list(set(list1))
print(tmp_list[len(tmp_list) - k])
# tmp_list.sort() # set already sort the list
# tmp_list.reverse()
# print(tmp_list[k-1])



