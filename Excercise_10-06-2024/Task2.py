# Python script that calculates the square and cube of a number

num = input("Enter a number: ")
a = int(num) ** 2
print(f"square of a number:{a}")

b = int(num) ** 3
print(f"cube of a number:{b}")

#python program to take the input for two number and print if num1 is greater than num2 or less than or equal to num2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("number1 is greater than number 2" if num1>num2 else "number1 is less than or equal to number 2" if num1<num2 else "number 1 is equal to number 2" if num1 == num2 else "invalid input")