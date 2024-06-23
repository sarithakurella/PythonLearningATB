#unpacking of tuple - we need that many variables to assing
a,b,c = (1,2,3)

#we wont be able to append the tuples as they are immutable
#So either we need to conevrt that to list or create a new tuple extending old one
t = (1, 2, 3)
my_list=list(t)
print(my_list)
my_list.append(4)
print(my_list)
t_new = tuple(my_list)
print(t_new)

t1=(10,20,30)
print(t1)
new_t1 = t1+(40,)
print(new_t1)
