def has_zero_sum_subarray(arr):
    cumulative_sum_set = set()
    cumulative_sum = 0
    for element in arr:
        cumulative_sum += element
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            print("YES")
            return
        cumulative_sum_set.add(cumulative_sum)

    print("NO")


N = int(input())
arr = list(map(int, input().split()))
has_zero_sum_subarray(arr)
# sum of elements between two identical cumulative sums is zero.