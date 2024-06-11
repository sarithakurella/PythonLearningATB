# Python script that calculates the square and cube of a number

num = input("Enter a number: ")
a = int(num) ** 2
print(f"square of a number:{a}")

b = int(num) ** 3
print(f"cube of a number:{b}")

#python script that takes two numbers as input and prints whether the first number is greater than or less than or equal to second number

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print ("num1 is greater than num2" if num1>num2 else "num1 is less than num2" if num1<num2 else "num1 is equal to num2" if num1==num2 else "invalid input")

