# Print the factorial of a number
num = int(input("enter a number: "))
res = 1
for num in range(1, num + 1):
    res = num * res
print("Factorial of a num :",res)
