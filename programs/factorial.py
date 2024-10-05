#--------------- Factorial -----------------

n = 6
result = 1
#------- loops -------------
for i in range(2,n+1):
    result *= i

print(result)


# ------- Recursion --------
def fact(n):
    if n == 1 or n == 0:
        return 1
    elif( n < 0):
        print("neg not allowed")
        return
    return n * fact(n-1)

print(fact(n))
    


