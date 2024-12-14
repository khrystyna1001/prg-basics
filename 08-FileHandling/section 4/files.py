# The files.txt contains a list of file names. 
# Write a program that prints only those file names whose extensions consist of exactly four 
# characters (e.g. .html).
import re

with open('files.txt', 'r') as file:
    content = file.readlines()


pattern = r'\.([a-zA-Z0-9]{4})$'
for file_name in content:
    if re.search(pattern, file_name):
        print(file_name)
