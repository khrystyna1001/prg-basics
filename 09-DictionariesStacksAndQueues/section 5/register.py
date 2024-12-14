import csv

d = {}
with open('province.csv', 'r', newline='', encoding='utf-8') as prov:
    csv_reader = csv.DictReader(prov)
    for row in csv_reader:
        letter = row['Letter'].upper()
        name = row['Name']
        d[letter] = name

vehicle_count = {}
with open('vehicle.txt', 'r', newline='', encoding='utf-8') as v:
    for line in v:
        rn = line.upper()
        fl = rn[0]
        if fl in d:
            name = d[fl]
            if name in vehicle_count:
                vehicle_count[name] += 1
            else:
                vehicle_count[name] = 1

for x, y in vehicle_count.items():
    print(f'{x} : {y}')