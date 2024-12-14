file_name = 'books.csv'

print('File name:', file_name)

lines = 0
words = 0
characters = 0
with open(file_name, 'r') as file:
    for line in file:
        lines +=1
        for character in line:
            characters += 1

with open(file_name, 'r') as file:
    content = file.read()

content_split = content.split()
for i in range(len(content_split)):
    words = i

print('Number of lines:', lines)
print('Number of words:', words)
print('Number of characters', characters)