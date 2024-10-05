# probelms related to getting the digits of num


# ----------------- sum of digits
# n = 3563

# sum = 0
# max = int(str(n)[0])
# for i in str(n):
#     sum += int(i)
#     if(int(i) > max):
#         max = int(i)

# print(sum)
# print('max is ',max)


# # --------
# temp = n
# sum = 0
# while(temp > 0):
#     sum+= temp%10
#     temp //= 10
# print(sum)



## ------------------ rever the digit -----------------------
# n = 12345
# temp = n
# reverse = 0
# while(temp > 0):
#     reverse = reverse*10 + temp%10
#     temp//=10
# print(reverse)

# # using string
# print(int(str(n)[::-1]))

# reverse2 = 0
# for i in str(n)[::-1]:
#     reverse2 = reverse2*10 + int(i)
# print(reverse2)



## ------------------ palindrom -----------------------
# n = input('enter a number :')
# print('palindrom') if(n == str(n)[::-1]) else print('not palindrom')

## ----------------- armstrong ------------------------
# n = 23

# def arms(n):
#     count = len(str(n))
#     sum = 0
#     for i in str(n):
#         sum+= int(i)**count
#     if(n == sum):
#         return True
#     else:
#         return False

# a = [i for i in range(1000, 10000)]
# print(list(filter(arms, a)))
