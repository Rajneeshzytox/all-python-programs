# list: print prime numbers till 300 and total no of primes 


# --------------- filter 

def isPrime(n:int, IsPrime=False):
    if(n<2):
        return False
    for i in range(2, int(n**0.5)+1):
        if(n%i == 0):
            IsPrime = False
            break
    else:
        IsPrime = True
    return IsPrime

a = [i for i in range(301)]

b = list(filter(isPrime, a))

print(b)
print(len(b))

# ---------------------------- 