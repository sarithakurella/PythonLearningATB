# Create a program that determines whether a given year is a leap year.

Year = int(input("Enter the year"))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
