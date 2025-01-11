stats = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

check = lambda x: x > 0
vals = list(filter(check, stats.values()))
find_name = lambda x: [name for name,val in stats.items() if val == x]

positive_cities = []
for val in vals:
    names = find_name(val)
    positive_cities.extend(names)

print(f"Cities with positive temperatures: {' '.join(set(positive_cities))}")