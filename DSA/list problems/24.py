# #ALL: Pattern


# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10

n = 4

example = [i for i in range(int((n**2 + n)/2)+1)]

def print_triangle(list1:list, n):
    ptr = 0
    for i in range(1,n+1):
        for j in range(i):
            print(list1[ptr], end=' ')
            ptr+=1
        print()

# print_triangle(example, n)

### ----------------------------------- ###
# Pattern 1: Fibonacci series in triangle
# 1st Pattern
# 2
# 3,5
# 8, 13, - 
# - , - , - , -

def fibo(n):
    total_count = int(((n)*(n+1))/2)
    fibo_list = []

    for i in range(total_count+2):
        if(i == 0 or i == 1):
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

    return fibo_list[2:total_count+2]

# print(fibo(n))

# print_triangle(fibo(n), n)



#############################################################
# pattern 2
# 0
# 1 4
# 2 5 8
# 3 6 9 10
# -------------------

def print_triangle_vertical(list1, n:int ):

    k = [0,2,3,3]
    for i in range(n):
        for j in range(i+1):
            index = i+j + k[j]
            print(list1[index], end=' ')
        print()

print_triangle_vertical(fibo(n), n)


###################

def isPrime(num:int):
    if(num<2):
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    else:
        return True


def prime_list_gen(n):
    total = int(((n)*(n+1))/2)
    num = 2
    prime_list = []

    while(len(prime_list) < total):
        if(isPrime(num)):
            prime_list.append(num)
        num+=1

    return prime_list


prime_num = prime_list_gen(n)

print_triangle_vertical(prime_num, n)
