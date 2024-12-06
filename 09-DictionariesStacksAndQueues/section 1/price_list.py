price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print(f"Prices before discount:")
for key, value in price_list.items():
    print(f"{key} : {value}")
print()

print("Total value:")
total = 0
for val in price_list.values():
    total += val
print(f"{total:.2f}")
print()

for key, val in price_list.items():
    price_list[f'{key}'] = val * 90 / 100

print("After the 10% discount:")
for key, value in price_list.items():
    print(f"{key} : {value:.2f}")
print()

print("Total value:")
totall = 0
for val in price_list.values():
    totall += val
print(f"{totall:.2f}")        