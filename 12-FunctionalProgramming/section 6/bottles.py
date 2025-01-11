print('Bottle capacity:    500ml')
print('Filling tolerance:  2%')
print('Filled bottles:     508,500,512,499,492,511,503,476,501,509')

bottles = [508,500,512,499,492,511,503,476,501,509]
capacity = 500
tolerance = 2

total = 0
for bottle in bottles:
    if bottle > capacity * (1 + tolerance/100) or bottle < capacity * (1 - tolerance/100):
        total += 1

print(f'Incorrectly filled: {total * 100 / len(bottles):.2f}%')