# test_list = [3, 4, 1, 7, 9, 1]
# print("The original list : " + str(test_list))

# # Using list comprehension + sum() + list slicing
# res = [sum(test_list[: i + 1]) for i in range(len(test_list))]

# print("The prefix sum list is : " + str(res))

# # Using accumulate(iterable) method.
# from itertools import accumulate
# res = list(accumulate(test_list))

# print("The prefix sum list is : " + str(res))

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())

    sum_range = prefix_sum[r] - prefix_sum[l - 1]
    print(sum_range)
