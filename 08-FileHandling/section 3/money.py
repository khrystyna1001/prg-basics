import re 

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8')  as email_content:
    email = email_content.read()

pattern = r'€\s?(\d+)'

amounts = re.findall(pattern, email)

total_spent = 0
for amount in amounts:
    amount = amount.replace(',', '')
    total_spent += int(amount)

print(total_spent)