array = list(map(int, input().split()))
subsequence = list(map(int, input().split()))


# O(n) time | O(1) space
def validateSubsequence(array, subsequence):
    sequeIdx = 0
    for i in array:
        if sequeIdx == len(subsequence):
            break
        if i == subsequence[sequeIdx]:
            sequeIdx += 1
    return sequeIdx == len(subsequence)


result = print(validateSubsequence(array, subsequence))

# O(n) time | O(1) space
# def validateSubsequence(array , subsequence):
#     aryIdx, seqIdx = 0, 0
#     while aryIdx<len(array) and seqIdx<len(subsequence):
#         if array[aryIdx] == subsequence[seqIdx]:
#             seqIdx += 1
#         aryIdx += 1
#     return seqIdx == len(subsequence)

# result = print(validateSubsequence(array,subsequence))
