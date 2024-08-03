def count_glasses(n, A):
    left = 0
    right = n - 1
    aman_drunk = 0
    bittu_drunk = 0
    aman_glasses = 0
    bittu_glasses = 0

    while left <= right:
        if aman_drunk <= bittu_drunk:
            aman_drunk += A[left]
            aman_glasses += 1
            left += 1
        else:
            bittu_drunk += A[right]
            bittu_glasses += 1
            right -= 1

    return aman_glasses, bittu_glasses


n = int(input())

A = list(map(int, input().split()))

aman_glasses, bittu_glasses = count_glasses(n, A)
print(aman_glasses, bittu_glasses)
