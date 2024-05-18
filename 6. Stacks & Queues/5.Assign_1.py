def find_corresponding_indices(bracket_sequence):
    n = len(bracket_sequence)
    result = [-1] * n
    stack = []
    for i in range(n):
        if bracket_sequence[i] == "(":
            stack.append(i)
        elif bracket_sequence[i] == ")":
            if stack:
                opening_index = stack.pop()
                result[opening_index] = i
                result[i] = opening_index
            else:
                result[i] = -1

    return result

bracket_sequence = input()
result = find_corresponding_indices(bracket_sequence)
print(*result)
