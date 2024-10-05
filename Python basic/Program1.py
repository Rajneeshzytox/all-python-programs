# """
# program to get a number from user and print its
#  -- hex
#  -- binary
#  -- octal
#  -- sq root
# """

number = int(input("enter a number: "))
print(f"hex value of {number} is {hex(number)}")
print(f"binary value of {number} is {bin(number)}")
print(f"octal value of {number} is {oct(number)}")
print(f"sqrt of {number} is {(number**(1/2))}")
