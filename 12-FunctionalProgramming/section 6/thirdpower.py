arr = [x for x in range(1, 21)]
third_power = lambda arr: arr**3
x = list(map(third_power, arr))

print(x)