# Write a program that classifies a triangle based on its side lengths.
X = int(input("Enter 1st side of triangle"))
Y = int(input("Enter 2nd side of triangle"))
Z = int(input("Enter 3rd side of triangle"))

if X == Y and Y == Z:
    print("The triangle is an equilateral triangle")
else:
    if X == Y or X == Z and Y != Z:
        print("The triangle is an isosceles triangle")
if X != Y and Y != Z and X != Z:
    print("The triangle is a scalene triangle")
