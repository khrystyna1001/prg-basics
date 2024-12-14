with open('it_company.csv', 'r') as file:
    lines = file.readlines()

index = 0
while index < len(lines):
    for i in range(index, min(index + 5, len(lines))):
        print(lines[i])

    x = input("\nPress Enter key...")

    if x != '':
        raise ValueError("You must press Enter key only, no other input is allowed.")
    index += 1