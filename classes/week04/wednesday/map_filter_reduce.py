#section 1 map()
nums = [1, 2, 3, 4]

# Lambda version
squared_iter = map(lambda x: x**2, nums)
print(squared_iter)          # <map object at 0x...>
print(list(squared_iter))    # [1, 4, 9, 16]

# Named function version
def square(x):
    return x**2

squared_iter = map(square, nums)
print(list(squared_iter))    # [1, 4, 9, 16]


#section 2 filter()
nums = [1, 2, 3, 4, 5, 6]

# Lambda version
evens_iter = filter(lambda x: x % 2 == 0, nums)
print(evens_iter)            # <filter object at 0x...>
print(list(evens_iter))      # [2, 4, 6]

# Named function version
def is_even(x):
    return x % 2 == 0

evens_iter = filter(is_even, nums)
print(list(evens_iter))      # [2, 4, 6]


#section 3 reduce
from functools import reduce

nums = [1, 2, 3, 4]

# Lambda version
product = reduce(lambda x, y: x * y, nums)
print(product)               # 24

# Named function version
def multiply(x, y):
    return x * y

product = reduce(multiply, nums)
print(product)               # 24
