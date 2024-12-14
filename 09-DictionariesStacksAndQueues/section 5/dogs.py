import json

with open('dogs.json', 'r', encoding='utf-8') as json_file:
    val = json.load(json_file)

for dog in val:
    if dog['age'] < 5:
        print(f'{dog['name']}, {dog['breed']}, {dog['weight_kg']}, {dog['owner']}, {dog['vaccinated']}')