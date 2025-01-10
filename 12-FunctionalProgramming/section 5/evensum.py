from functools import reduce

numbers = [2,4,6,3,7,5]
filtered_nums = lambda y: filter(lambda x: x%2 == 0, y)
filtered = list(filtered_nums(numbers))
res = reduce(lambda a,b: a + b, filtered)
print(res)