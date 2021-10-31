# fruits = ['apple', 'banna', 'kiwi', 'aaaa', 'bbbb']

# result = [x * 5 for x in fruits if 'a' in x]
# # for x in fruits:
# #     if 'a' in x:
# #         result.append(x)

# print(result)


# square_dict = {x: x**2 for x in range(1,11)}
# print(square_dict)

# def is_odd(x):
#     return x % 2 == 0

#     # if x % 2 == 0:
#     #     return True
#     # else:
#     #     return False    

# print(is_odd(122))    


# def factorial(n):
#     if n in (1, 0):
#         return 1
#     return factorial(n-1) * n

# print(factorial(10))


# n = 30
# recursion_count = 0

#     global recursion_count
#     recursion_count = 1
# def fib(x):

#     return fib(x-1) + fib(x-2)

# print(fib(30))


# def print_func(a, b, c, d=100, e=100):
#     print(a, b, c, d, e)

# print_func(1, 2, 3, 4, 5)
# print_func(1, 2, 3, 4)
# print_func(1, 2, 3)


# def func(a, b, c, *args, **kwargs):
#     print(type(args))
#     print(args (kwargs))
#     print(args, kwargs)

# func(1, 2, 3, 123, 123, 32, g=123, d=4123)


# def swap(a, b):
#     return b, a
# result = swap(1, 2)
# print(result)


# function = lambda **kwargs: max(kwargs.value)
# print(function(10, 11, 123, 9999, -100))


# try:
#     a = 3/0
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ValueError:
#     print('ValueError')
# except Exception as e:
#     print(f'Unknown error: {e}')
# else:
#     print('Everything ok!')
# finally:
#     print('End of life')

#     print('After error')


# from os import environ as environment

# print (environment.keys())


import sys
print(dir(sys))