def reverseds(string):
    stack = []
    for char in string:
        stack.append(char)
    reversedstr = ''
    while stack:
        reversedstr += stack.pop()
    return reversedstr

input_string = input('Enter a message: ')
reversed_string = reverseds(input_string)
print(f"Reversed text: {reversed_string}")