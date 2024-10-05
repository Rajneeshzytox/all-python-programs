#----------------- finding prime numbers -----------------
# prime no. 2,3,5...
# n is prime when n does not divisible by any no. btw [2, root(n)]
# n > 2

# grtting the no. 
# n = 3.0
# isPrime = True
#---------- loops:
# for i in range(2, int(n**0.5) + 1):
#     if(n%i == 0):
#         print(n, ' is divible by ', i)
#         isPrime = False
#         break
    
# if isPrime:
#     print(n, ' is prime no')
# else:
#     print(n, ' is not prime no')


# -------------- Function -------------------

# def checkPrime(n:int , isPrime=True) -> bool:
#     if(n<2):
#         isPrime = False
#     elif(n - int(n)):
#         print('number cant be float')
#         return False
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if(n%i == 0):
#                 print(f"{n} is divible by {i}")
#                 isPrime = False
#                 break
#     return isPrime

# if checkPrime(n):
#     print(n, ' is prime no')
# else:
#     print(n, ' is not prime no')




# -------------- Recursion -------------------

# def checkPrime(n, i=2):
#     if n==2:
#         return True
#     elif(n<2) or (n%i == 0):
#         return False
#     elif(i > int(n**0.5)):
#         return True
#     return checkPrime(n, i+1)

# a ='yes number is prime' if (checkPrime(121)) else 'Not prime' 
# print(a)
# ----------------------------------------
# n = 2
# i = n-1
# def checkPrime(n, i):
    
#     if(n<2):
#         return False
#     elif( i < 2):
#         return True
#     elif(n%i == 0):
#         return False
#     return checkPrime(n, i-1)

# print('yes') if (checkPrime(n, i)) else print('no')