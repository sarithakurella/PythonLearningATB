# Ternary operator

# calculate the area of a circle
# input is radius
# output is area
# data type - lets go with folat
# formula - area = pi * r * r

import math

radius = float(input("enter the radius"))
area = math.pi * (radius * 2)
print(area)

# above can be done in one line

print(math.pi * (float(input("enter the radius\n")) ** 2))
