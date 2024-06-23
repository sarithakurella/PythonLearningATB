#Tuple and decorators

#Tuple is similar to list which is with only braces and cannot be changed with the values at any point of time
#Real example is we can use all the list of API URL's in a tuple and can call them directly which ususally doesnt change much

API_URLs = ('https://api.example.com', 'https://api2.example.com')
print(API_URLs[0])

#Conversion of list to tuple

list1 = [1,2,3,4,5]
print(list1)
t1 =tuple(list1)
print(t1)



