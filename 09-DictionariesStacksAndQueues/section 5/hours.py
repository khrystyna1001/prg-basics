winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

t = 0
for x in winter_semester.values():
    t += x

print(f'The total number of hours in the winter semester is {t}')