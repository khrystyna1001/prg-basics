employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title = 'Software Engineer'

with open(employees_file, 'r') as text:
    with open(position_file, 'w') as file:
        for line in text:
            if job_title in line:
                file.write(line)