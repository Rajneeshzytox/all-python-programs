# list: find majority

a = [4,3,2,3,2,4,2,1,3,5,1,5,2,4]



# ------------------------- approach 1: using count()
def majority1(a:list):
    set_a = set(a) # just to get unique val
    majority_count = float('-inf')
    majority = float('-inf')
    for i in set_a:
        count = a.count(i)
        if(count > majority_count):
            majority_count = count
            majority = i
    return majority, majority_count

print(majority1(a))


