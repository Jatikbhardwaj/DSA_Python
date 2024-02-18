# Brute force solution  O(n^2) time | O(1) space:-
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []


# array = list(map(int, input().split()))
# targetSum = int(input())
# result = twoNumberSum(array, targetSum)
# print(result)


# Hashing O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in range(len(array)):
        Match = targetSum - array[num]
        if Match in nums:
            return [Match, array[num]]
        else:
            nums[array[num]] = True
    return []


array = list(map(int, input().split()))
targetSum = int(input())
result = twoNumberSum(array, targetSum)
print(result)


# When array is sorted:-
# array = list(map(int,input().split()))
# target = int(input())
# def two_sum(array: list, target: int):
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         current_sum = array[left] + array[right]
#         if current_sum < target:
#             left += 1
#         elif current_sum > target:
#             right -=1
#         else:
#             print("Yes")
#             return
#     print("No")

# two_sum(array, target)

# TC = O(n)
# SC = O(1)
