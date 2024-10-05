# Program to calculate area of triangle

# heron formula: sqrt(s*(s-a)*(s-b)*(s-c))/
# s = (a+b+c)/2

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))
if ( a >= 0 or b >= 0 or c >= 0):
    s = float((a + b + c)/2)
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(f"\nArea of triangle with sides \n{a}cm \n{b}cm \n{c}cm is\n{'area':-^30}\n{area}cm^2")
else:
    print("invalid inputs")