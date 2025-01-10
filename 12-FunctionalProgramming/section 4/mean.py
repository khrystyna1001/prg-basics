import statistics
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

f = lambda x: filter(lambda grade: grade != 2.0, x)
filtered = list(f(grades))
sm = round((statistics.mean(filtered)), 2)

print(f'Arithmetic mean for grades <> 2.0 is {sm}')