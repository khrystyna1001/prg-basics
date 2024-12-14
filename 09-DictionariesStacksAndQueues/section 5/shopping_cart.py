prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

cart = {'juice': 3, 'bread': 1, 'milk': 2}

t = 0
for x, y in cart.items():
    if x in prices:
        t += y * prices[x]
print(f'Total cost: {t}')