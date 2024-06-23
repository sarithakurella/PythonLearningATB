#
def say_hello_args_default(name = "saritha"):
    print(f"Hello {name}")

#default be taken here from function
say_hello_args_default()
#it will take the value if we pass
say_hello_args_default("Sita")
#We can pass the arguments as below also
say_hello_args_default(name="Ram")
