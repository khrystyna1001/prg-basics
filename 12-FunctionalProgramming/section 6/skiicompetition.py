points = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

calc = lambda points:sum(sorted(points)[1:4])

print(list(map(calc, points)))