import csv

with open('clothing.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row['Price'] < '60' and row['Stock_Quantity'] < '40':
            print(f'{row['Product_ID']}, {row['Product_Name']}, {row['Category']}, {row['Size']}, {row['Color']}')