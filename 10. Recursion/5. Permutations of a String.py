def generate_permutations(s):
    # Base case: if the string has only one character, return it as a list
    if len(s) == 1:
        return [s]

    # List to store all permutations
    permutations = []


    # Try each character as the first character
    for i in range(len(s)):
        # Choose the current character
        print(f"i: {i}")
        first = s[i]
        print(f"first: {first}")

        # Get the rest of the string (excluding the chosen character)
        rest = s[:i] + s[i + 1:]
        print(f"s[:i]: {s[:i]}")
        print(f"s[i + 1:] {s[i + 1:]}")
        print(f"rest: {rest}")

        # Recursively generate permutations for the rest of the string
        for perm in generate_permutations(rest):
            # Append the chosen character to each permutation of the rest
            permutations.append(first + perm)
            print(f"permutations:{permutations}")

    return permutations

    # Read input string


s = input().strip()

# Generate all permutations
all_permutations = generate_permutations(s)

# Sort permutations lexicographically
all_permutations.sort()

# Print each permutation
for perm in all_permutations:
    print(perm)
