# n = int(input())
# array = list(map(int,input().split()))
# k = int (input())
# max_sum = float('-inf')

# for i in range(n-k+1):
#     curr_sum = 0
#     for j in range(i,k+i):
#         curr_sum += array[j]
#     max_sum = max(max_sum,curr_sum)

# print(max_sum)

# TC = O(n*k)
# SC = O(1)

# USING SLIDING WINDOW TECHNIQUE 

n = int(input())
array = list(map(int,input().split()))
k = int (input())
max_sum = float('inf')




