# list: find duplicate
# input = [4,3,2,7,8,2,3,1]
# output = {2: 2, 3: 2}

input = [4,3,2,7,8,2,3,1,3,3, 4]

def just_tell_if_duplicate(a):
    output = []
    a = sorted(a)
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            output.append(a[i]) if a[i] not in output else 'do nothing'
            
    return output
print(just_tell_if_duplicate(input))

#--------------------------- Program to represent what is duplicate and how many times in dictionary
def how_many_duplicates(a):
    output = {}
    a = sorted(a)
    len_a = len(a)

    for i in range(len_a):
        if(i == len_a - 1 or a[i] != a[i+1]):
            continue
        count = 0
        j = i+1
        while(j < len_a and a[i] == a[j]):
            count += 1
            j += 1
        output.setdefault(a[i], count+1)
    
    return output

print(how_many_duplicates(input))

#--------------------------- Program to represent what is duplicate and how many times usingg set
def how_many_duplicates_using_set(a:list):
    # -----gives all number and how many times they repeat-----
    # new_a = set(a) # if you want like this {1: 1, 2: 2, 3: 4, 4: 2, 7: 1, 8: 1}

    # ----ust give the duplicate value and how many times repeat----
    new_a = just_tell_if_duplicate(a) # {2: 2, 3: 4, 4: 2}

    output = {}
    
    for i in new_a:
        output.setdefault(i, a.count(i))

    return output
        
print(how_many_duplicates_using_set(input))
