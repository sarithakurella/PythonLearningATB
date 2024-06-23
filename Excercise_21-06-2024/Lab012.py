#Dict
#key value pair
#name ->pramod
my_dict = {'name':'pramod','age':25}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.keys())
print(my_dict.values())
print(len(my_dict))

for i in list(my_dict.keys()):
    print(i)


for j in list(my_dict.values()):
    print(j)

for i,j in my_dict.items():
    print(i,j)
#in list we used to get the details using index, but in dict we use key to get the details

#we can have duplicate values but we wont be able to have duplicate keys

my_dictionary = {
    'name': 'pramod',
    'age': 25,
    'age': 30
}
print(my_dictionary)

#it will print the latest value of the key

my_dictionary = {'name':'pramod','age':25,'no of books':'25'}
print(my_dictionary)

