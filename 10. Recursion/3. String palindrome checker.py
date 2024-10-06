def check_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s, left + 1, right - 1)


s = input()
result = check_palindrome(s, 0, len(s) - 1)
print(result)

# T.C :- O(n)
# S.C :- O(n)
