def integer_sqrt(X):
    def predicate(M):
        return 0 if M * M <= X else 1

    L = 0  # start from 0 since sqrt(X) > 0 for X > 0
    R = X

    while L + 1 < R:
        M = L + (R - L) // 2
        if predicate(M) == 0:
            L = M
        else:
            R = M

    return L


print(integer_sqrt(17))  # Output: 4


# T.C = O(log X)

# Square Root with Decimal Precision
# We can modify the algorithm to work with floating-point numbers and a specified precision:
def sqrt_with_precision(X, epsilon=1e-6):
    def predicate(M):
        return 0 if M * M <= X else 1

    L = 0
    R = max(1, X)  # we need max(1, X) to handle X < 1

    while L + epsilon < R:
        M = L + (R - L) / 2
        if predicate(M) == 0:
            L = M
        else:
            R = M

    return L


print(f"{sqrt_with_precision(17):.6f}")  # Output: 4.123106
print(f"{sqrt_with_precision(0.25):.6f}")  # Output: 0.500000
# For square root with E decimal places: O(log(X/E))
# The problem is monotonous, making it suitable for binary search.
# The predicate function M * M <= X correctly divides the search space.
# For decimal precision, we adjust the while loop condition to L + epsilon < R.
# We use R = max(1, X) to handle cases where X < 1.