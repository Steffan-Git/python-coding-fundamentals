#  Repeatability, contracts, abstraction. 

# def greet(name: str, age: int) -> str: #params go here, args are passed through when function is called. 
#     """ Returns a greeting"""
#     return f"hello {name}, age is {age}"

# print(greet(10, "c")) #positional - needs to be in the correct order. 
# print(greet(age=10, name="c")) #keyword - order doesnt matter.

# def greet(name, age=10):
#     return f"hello {name}, age is {age}"
# x = greet("c")
# print(x)

# *args
# sends a tuple of args to be unpacked - 
# used for when we dont know how many args there will be.

# def pizza_order(size, *toppings):
#     print(f"Order for {size}-size pizza with toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# pizza_order("med", "mushrooms")

# **kwargs - when we dont know how many key word args will be used. 
# - sends dictionary.

# def api_call(url, method="GET", **kwargs):
#     print("Making API call...")
#     print("URL:", url)
#     print("Method:", method)
#     print("Extra options:", kwargs)

# api_call(
#     "https://api.example.com/users",
#     method="PUT",
#     headers={"Authorization": "Bearer 123"},
#     cookies={"session_id": "abc"}
# )
# print()

# def combined(*args, **kwargs):
#     print(args)
#     print(kwargs)

# combined(z=1, d=2, h=3, a=4, b=5)

# control user calling behaviour:
# / anything before / must be a positional arg.  
# * anything after * must be a keyword arg.
# THIS IS ENFORCED.

# def example(a, b, /, c, d=10, *, e, f):
#     print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

# example(a=1, b=2, c=2, d=4, e=5, f=6)

# def maths_op(a, b, /, operation: str ="add", *, decimal_place=None):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise ValueError("Unsupported operation")
#     return round(result, decimal_place)

# print(maths_op(5, 5))
# print(maths_op(5,5, "subtract"))
# print(maths_op(5, 5, operation="add"))
# print(maths_op(5.15687, 5.232656, operation="add", decimal_place=4))


# Recursion:

# def factorial(n: int) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120 
     
# frame:  - store local variables and function state.
#         - locals() and globals()
#         - calling context:
#             - code object = (f_code)


# stack: stack of frames, ordered by call time.
# pops the function. 


# import inspect

# def trace_function_calls():
#     print("current frame info:",  inspect.currentframe().f_code.co_name)
#     print("stack info:", inspect.stack()[0].function)
#     x = 5
#     print(locals())
#     for frame in inspect.stack():
#        print(frame.function)

# def caller():
#     trace_function_calls()

# caller()
# print(locals())

# higher level functions:

# def square(x):
#     return x * x

# def apply_function(func, value):

#     return func(value)

# print(apply_function(square, 5))  # Output: 25

# lambdas: discrete, one line, unnamed(mostly) functions.

# square = lambda x: x * x
# print(square(6))  # Output: 36

# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_numbers = list(map(lambda x: x ** 2, numbers))


# wrappers:

# def simle_wrapper(func):
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simle_wrapper
# def greet(name):
#     """
#     Returns a greeting message.
#     """
#     print(f"Hello, {name}!")
    
# print(greet.__doc__)  # Output: Returns a greeting message.
# greet(  "Alice") 

# from functools import wraps, lru_cache
# import time

# def simle_wrapper(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simle_wrapper
# def greet(name):
#     """
#     Returns a greeting message.
#     """
#     print(f"Hello, {name}!")
    
# print(greet.__doc__)  # Output: Returns a greeting message.
# greet(  "Alice")

# @lru_cache(maxsize=None)
# def add(a, b):
#     print("Computing...")
#     time.sleep(10) # Simulate a time-consuming computation
#     return a + b

# print(add(5, 10))  # Computes and caches the result
# print(add(5, 10))  # Retrieves the result from the cache
