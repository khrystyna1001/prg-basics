hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

print('Hotels in Krakow: ')
keys = [d['name'] for d in hotels_in_Krakow]
for i, key in enumerate(keys):
    print(key, end='')
    if i < len(keys) - 1:
        print(', ', end='')
print()
print('Average hotel price in Krakow: ')
s = 0
for row in hotels_in_Krakow:
    s += row['price']
print(s)
print('Hotels in Sopot: ')
keys = [d['name'] for d in hotels_in_Sopot]
for i, key in enumerate(keys):
    print(key, end='')
    if i < len(keys) - 1:
        print(', ', end='')
print()
print('Average hotel price in Sopot: ')
t = 0
for row in hotels_in_Sopot:
    t += row['price']
print(t)
print('Cheaper hotels in: ')
if s > t:
    print('Sopot')
else:
    print('Krakow')