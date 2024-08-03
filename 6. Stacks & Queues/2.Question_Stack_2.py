def push(stack, max_stack, x):
    stack.append(x)
    if not max_stack or x >= max_stack[-1]:
        max_stack.append(x)


def pop(stack, max_stack):
    if not stack:
        return None
    popped_element = stack.pop()
    if popped_element == max_stack[-1]:
        max_stack.pop()
    return popped_element


def get_max(max_stack):
    if not max_stack:
        return None
    return max_stack[-1]


n = int(input())
element_stack = []
max_stack = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        push(element_stack, max_stack, x)
    elif query[0] == '2':
        pop(element_stack, max_stack)
    elif query[0] == '3':
        print(get_max(max_stack))
