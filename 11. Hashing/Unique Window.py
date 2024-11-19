def count_unique_elements_in_windows(N, K, A):
    # Initialize a dictionary to store the frequency of elements in the current window
    frequency = {}

    # List to store the result of unique counts for each window
    unique_counts = []

    # Initialize the frequency dictionary for the first window
    for i in range(K):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1

    # Add the count of unique elements in the first window to the result list
    unique_counts.append(len(frequency))

    # Slide the window from left to right
    for i in range(K, N):
        # Remove the first element of the previous window
        first_elem = A[i - K]
        frequency[first_elem] -= 1
        if frequency[first_elem] == 0:
            del frequency[first_elem]

        # Add the new element of the current window
        new_elem = A[i]
        if new_elem in frequency:
            frequency[new_elem] += 1
        else:
            frequency[new_elem] = 1

        # Append the count of unique elements in the current window to the result list
        unique_counts.append(len(frequency))

    return unique_counts


N, K = map(int, input().split())
A = list(map(int, input().split()))
result = count_unique_elements_in_windows(N, K, A)
print(*result)
