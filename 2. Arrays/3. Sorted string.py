# def sorted_string(input_string: str):
#     sorted_letters = ''.join(sorted(input_string))
#     return sorted_letters
# input_string  = input()
# print(sorted_string(input_string))

# TC = O(nlogn)
# SC = O(n)

# Implementing using frequency table 
def sorted_string(input_string):
    letter_counts = [0] * 26
    for char in input_string:
        index = ord(char.lower()) - ord('a')
        letter_counts[index] += 1
    sorted_letters = ''
    for i in range(26):
        sorted_letters += chr(ord('a') + i) * letter_counts[i]
    return sorted_letters


input_string = input()
print(sorted_string(input_string))

# TC = O(n)
# SC = O(1)
# Solution 1 is better if length of possible characters in string is very very large

# Here are some scenarios where a frequency table can be useful in DSA (Data Structures and Algorithms):

# Sorting without comparison:

# Instead of using traditional sorting algorithms (like quicksort or mergesort), you can use a frequency table to sort elements based on their counts. This is especially useful when the range of values is small.
# Counting Sort:

# Counting Sort is a linear-time sorting algorithm that uses a frequency table to count the occurrences of each element in the input array. It is efficient when the range of input elements is known and not too large.
# String manipulation:

# In problems involving strings, you can use a frequency table to count the occurrences of characters. This is useful in anagrams, palindrome checks, and other string-related algorithms.
# Histograms and distribution problems:

# In problems related to data distribution or histograms, a frequency table can be used to efficiently count the occurrences of each value in a dataset.
# Frequency-based problems:

# Problems where you need to find the most frequent element, elements with certain frequencies, or any task related to frequency analysis can benefit from using a frequency table.
# Caching or memoization:

# In dynamic programming or recursive algorithms, a frequency table can be used to cache or memoize intermediate results to avoid redundant calculations and improve the overall efficiency of the algorithm.
# Optimizing algorithms:

# Frequency tables can be used to optimize certain algorithms by reducing the time complexity. For example, finding duplicate elements, checking if two arrays are permutations of each other, etc.
