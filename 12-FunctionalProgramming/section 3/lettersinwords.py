text = "I completely agree with you"

sentence = text
result = list(map(lambda x: len(x), sentence.split()))
print(sentence)
print(f'No. of letter in words: {result}')