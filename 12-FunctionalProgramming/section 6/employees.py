employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

formatted_employees = list(map(lambda y: f'{y[0].upper()}, {y[1]}', employees))
print(formatted_employees)