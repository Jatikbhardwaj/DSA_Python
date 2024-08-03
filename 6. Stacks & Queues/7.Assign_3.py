def evaluate_postfix(expresssion):
    stack = []
    for char in expresssion:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(int(a / b))
    return stack[-1] if stack else None


expression = list(map(str, input().split()))
result = print(evaluate_postfix(expression))
