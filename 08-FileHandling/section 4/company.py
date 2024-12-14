import csv

with open('it_company.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    print('GRAPHIC DESIGNERS')
    print('=================')

    for row in csv_reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f'{row['First Name']}, {row['Last Name']}, {row['Email']}')