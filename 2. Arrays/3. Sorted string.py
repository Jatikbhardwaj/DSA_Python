def sorted_string(input_string: str):
    sorted_letters = ''.join(sorted(input_string))
    return sorted_letters
input_string  = input()
print(sorted_string(input_string))

# TC = O(nlogn)
# SC = O(n)
