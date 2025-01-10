arr = [x for x in range(1, 21)]
filtered_arr = filter(lambda y: y%2 == 0 and y%3 == 0, arr)
print(list(filtered_arr))