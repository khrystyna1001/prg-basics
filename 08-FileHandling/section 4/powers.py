# 1,1,1
# 2,4,8
# 3,9,27
# ...
# ...

with open('powers.txt', 'w') as file:
    for x in range(1, 101):
        sq = x ** 2
        cb = x ** 3

        print(f'{x}, {sq}, {cb}')
        file.write(f'{x}, {sq}, {cb}\n')