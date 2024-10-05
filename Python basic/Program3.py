# Program to calculate distance between points
# distance(x,y): sqrt((x2-x1)^2 + (y2-y1)^2)

x1 = float(input("enter coordinates of x1: "))
y1 = float(input("enter coordinates of y1: "))
x2 = float(input("enter coordinates of x2: "))
y2 = float(input("enter coordinates of y2: "))

distance = lambda x1, y1, x2, y2: (((x2-x1)**2) + ((y2-y1)**2))**0.5

print(f"distance between co ordinates ({x1}, {y1}) and ({x2}, {y2}) is")
print(f"{'distance':_^30}\n{distance(x1,y1,x2,y2):.2f}")