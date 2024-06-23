import time
def note_time_taken_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken : {end - start} seconds")
    return wrapper()
@note_time_taken_decorator
def my_function():
    time.sleep(3)
    print("time passed")

#decorators can be used as many times for any functions
@note_time_taken_decorator
def my_func2():
    time.sleep(2)
    print("second time")
