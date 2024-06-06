# print any no of args in the single print line - *Args takes any no of args
print("Saritha", "kurella", 12345, 4.9674, True)

# Above line is print with spaces as separater. Now try with sep
print("Saritha", "kurella", 12345, 4.9674, True, sep="$")
print("Saritha", "kurella", 12345, 4.9674, True, sep="-")
print("Saritha", "kurella", 12345, 4.9674, True, sep=" # ")

# working with multiple lines
print("print the first line")
print("print the second line")
print("print the third line")
print("Print the first line doesnt have new line", end='-')
print("print in the same line")

#try to concatenate lines with out any character
print("try to", end="")
print("concatenate lines")
