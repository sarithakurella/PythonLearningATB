def say_hello_arg_return(a, b):
    return a + b

res = say_hello_arg_return(2, 3)
print(res)

res1 = say_hello_arg_return(b=6,a=3)
print(res1)

print(say_hello_arg_return(3, 4))
