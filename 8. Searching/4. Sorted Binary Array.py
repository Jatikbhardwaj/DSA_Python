n = int(input())
arr = input().split()
L = -1
R = len(arr)
while L + 1 < R:
    M = (L + R) // 2
    if arr[M] == '0':
        L = M
    else:
        R = M
first_one = R
last_zero = L

if first_one == n:
    first_one = n
if last_zero == -1:
    last_zero = -1

print(f"{first_one} {last_zero}")