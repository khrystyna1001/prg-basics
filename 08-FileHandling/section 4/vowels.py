import re

text = input('Enter any sort of text: ')

pattern = r'[aeiouyAEIOU]'

pattern_match = re.findall(pattern, text)

count = len(pattern_match)

print(f'text has {count} vowels')