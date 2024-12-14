basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = basic_data.copy()
person.update(advanced_data)

for x, y in person.items():
    print(f'{x} : {y}')