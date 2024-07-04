import math 
n = float(input("Number of sides: "))
a = float(input("The length: "))

def deg_to_rad(n):
    rad = n*(math.pi*(1/180))
    return rad
if n>2:
    apothem = a/(2*(math.tan(deg_to_rad(180/n))))
    area = (n*a*apothem)/2
else: print("Such polygon doesn't exist")
print(area)