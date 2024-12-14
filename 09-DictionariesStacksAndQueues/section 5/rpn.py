stack = []
def rpn(expression):
    expression = expression.split()
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            if char == '/':
                stack.append(operand1 / operand2)
        elif char == '=':
            result = stack.pop()
            print(f'Result: {result}')
            return result
        else:
            print(f"Invalid char: {char}")
            return None
        
rpn('2 3 + =')
rpn('2 4 1 + * =')
rpn('2 3 + 4 5 + * =')
rpn('8 3 1 + / 3 2 - 4 + * =')