# list: find missing number
# missing num in list from 0 to n
# ex = 
#   input = [3,0,1]
#   output = [2]


# ---------- APPROACH 1 (set difference)
n = 7
a = [3,0,1] # output should be 2
b = set(a)
c = set([i for i in range(n+1)])

print(f"missing no. in list {a} upto {n} are  {list(c.difference(a))}")

# ---------- Approach 2 (sum)
n = 5
list1 = [4,5,2,0,1]

sum_upto_n = (n*(n+1))//2
sum_of_list = sum(list1)

missing_no = sum_upto_n - sum_of_list
print(f'missing no. in {list1} upto {n} is {missing_no}')
