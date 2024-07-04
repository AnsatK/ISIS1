import math
def deg_to_rad(n):
    rad = n*(math.pi*(1/180))
    return rad

n = float(input("Enter a number "))
print(deg_to_rad(n))