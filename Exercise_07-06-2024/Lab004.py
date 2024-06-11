
a = input("Enter the name")
print(a)
#always the result of input function is a string
print(type(a))

#using different functions to print the string
print(len(a))
print(id(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.swapcase())

#to print the num of times that particular character is repeated in the string
b = a.count('a')
print(b)

#how to print the certain charater from teh string by passing the index
print(a[2])

