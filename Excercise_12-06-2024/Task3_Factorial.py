# Print the factorial of a number
num = int(input("enter a number: "))
res = 1
for num in range(1, num + 1):
    res = num * res
print("Factorial of a num :",res)

# Print the factorial of a number
num = int(input("enter a number: "))
res = 1
printMultiplication=""
for i in range(num,0,-1):
    res = num * res
    printMultiplication+=str(i)+"*"
if(printMultiplication.endswith("*")):

    lengthOfTheString=len(printMultiplication);

    print(printMultiplication[0:(lengthOfTheString-1)])

else:

    print(printMultiplication)



print("Factorial of a num :",res)


