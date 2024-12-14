import json

movie = {
    "Name": "Arcane",
    "Main cast": ["Vi", "Caitlyn", "Ekko", "Jinx", "Jayce", "Viktor"],
    "Rating": "9/10",
    "Seasons": 2,
    "Episodes": 18
}

with open('favorite_movie.json', 'w', encoding='utf-8') as file:
    json.dump(movie, file, ensure_ascii=False, indent=4)