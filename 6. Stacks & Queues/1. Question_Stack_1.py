def check_sequence(in_seq, out_seq):
    i = 0
    j = 0
    stack = []

    while i < len(in_seq):
        if in_seq[i] == out_seq[j]:
            i += 1
            j += 1
        else:
            if stack and stack[-1] == out_seq[j]:
                stack.pop()
                j += 1
            else:
                stack.append(in_seq[i])
                i += 1

    while stack and stack[-1] == out_seq[j]:
        stack.pop()
        j += 1

    if not stack and j == len(out_seq):
        return "Yes"
    else:
        return "No"
    
n = int(input())
# in_seq = []
# for _ in range(n):
#     in_seq.extend(map(int, input().split(',')))
# out_seq = []
# for _ in range(n):
#     out_seq.extend(map(int, input().split(',')))
in_seq = list(map(int, input().split(',')))
out_seq = list(map(int,input().split(',')))
result = check_sequence(in_seq, out_seq)
print(result)

# T.C = O(N)
# S.C = O(N)