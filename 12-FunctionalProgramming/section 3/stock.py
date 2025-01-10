prods = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total = lambda t: sum(map(lambda x: x[0] * x[1], t))

print(f'Products in stock: {prods}')
print(f'Total value: {total(prods)}')