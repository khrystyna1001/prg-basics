test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

def min_pts(pts1, pts2):
    return lambda pts: pts['result']>=pts1 and pts['result']<=pts2

check = filter(min_pts(50, 70), test_results)
good_students = []
for student in check:
    good_students.append(student['name'])
    
print(good_students)