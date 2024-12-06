countries = [
    {"name":"Poland", "population":38000000},
    {"name": "USA", "population":334900000},
    {"name": "China", "population":1400000000},
    {"name": "Germany", "population":84000000},
    {"name": "France", "population":68000000}
]

for v in countries:
    for key, value in v.items():
        print(f"{key} : {value}")
    print()