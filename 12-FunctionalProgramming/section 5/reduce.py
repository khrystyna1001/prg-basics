from functools import reduce

add = lambda x, y: x + y

numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)
print(result)