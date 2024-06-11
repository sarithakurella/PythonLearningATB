shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(len(shopping_list))
print(shopping_list)
print(shopping_list[2])

#can have different data types in a list
shopping_list = ["milk", 5,  3.465, True , None]
print(shopping_list)

# functions in list
shopping_list.append("cookies")
print(shopping_list)
# to reverse the string
shopping_list.reverse()
print(shopping_list)
#insert with any items in the list
shopping_list.insert(3,'chocolates')
print(shopping_list)
# extends the list with any no of items we assign
shopping_list.extend(["chips", "sugar"])
print(shopping_list)
# remove - removes a particular item from list
shopping_list.remove("cookies")
print(shopping_list)
# pop removes last item
shopping_list.pop()
print(shopping_list)
#sorting the items in the list - unable to sort as it has none, boolean etc data types
#shopping_list.sort()
#print(shopping_list)
#clears the list completly
shopping_list.clear()
print(shopping_list)



