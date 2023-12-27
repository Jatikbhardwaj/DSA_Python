# Find the smallest natural number that is not present in a given array of integers. The array may not be sorted, and natural numbers are positive integers.
# Input
# 7
# 6 7 5 9 3 2 8
# Output
# 1
n = int(input())
array = list(map(int, input().split()))
my_dict = {i: False for i in range(1, n + 2)}
for i in range(n):
    if array[i] >= 1 and array[i] <= n:
        my_dict[array[i]] = True
for j in range(1, n + 2):
    if my_dict[j] == False:
        break
print(j)

# TC : O(n)
# SC : O(n)
