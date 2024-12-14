import json

with open('reservations.json', 'r', encoding='utf-8') as json_file:
    val = json.load(json_file)

reservations = val['reservations']

total = 0
paid = 0
unpaid = 0
t_paid = 0
t_unpaid = 0

for reservation in reservations:
    total += 1
    if reservation['paid']:
        paid += 1
        t_paid += reservation['price_per_night'] * reservation['nights']
    else:
        unpaid += 1
        t_unpaid += reservation['price_per_night'] * reservation['nights']

print(f'Total number of rooms: {total}')
print(f'Total number of paid reservations: {paid}')
print(f'Total number of unpaid reservations: {unpaid}')
print(f'Total value of paid reservations: {t_paid}')
print(f'Total value of unpaid reservations: {t_unpaid}')