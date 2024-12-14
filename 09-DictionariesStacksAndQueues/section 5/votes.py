import json

with open('votes.json', 'r', encoding='utf-8') as json_file:
    votes = json.load(json_file)

person_name = input('Name of the person you are voting for:')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open('votes.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(votes, jsonfile, ensure_ascii=False, indent=4)

print('Updated voting data')