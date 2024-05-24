def min_owners_to_contact(n,k,sizes):
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(n):
        current_sum += sizes[end]

        while current_sum >= k:
            min_length = min(min_length,end-start +1)
            current_sum -= sizes[start]
            start += 1
    return min_length if min_length != float('inf') else -1

# Input reading
n, k = list(map(int,input().split()))
sizes = list(map(int, input().split()))

# Calculating the result
result = min_owners_to_contact(n, k, sizes)

# Output the result
print(result)