def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
result = fibonacci(n)
print(result)

# T.C :-  O(2^n)
# S.C :- O(n)
#
# The time complexity of the naive recursive Fibonacci function is O(2^n). This is because:
#
# Each call to fibonacci(n) results in two further calls: fibonacci(n - 1) and fibonacci(n - 2).
# This creates a binary tree of calls, leading to an exponential growth in the number of calls as n increases.
# 2^0+ 2^1+2^2....2^n calculated as sum of GP so approx:- O(2^n)
