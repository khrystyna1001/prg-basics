res = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

print(f'Min 70 pts: {list(filter(min_pts(70), res))}')
print(f'Min 40 pts: {list(filter(min_pts(40), res))}')
print(f'Min 30 pts: {list(filter(min_pts(30), res))}')