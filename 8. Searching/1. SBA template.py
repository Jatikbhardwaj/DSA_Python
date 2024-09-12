# def binary_search_first_one(n, arr):
#     L = -1
#     R = n
#     while L + 1 < R:
#         M = (L + R) // 2
#         if arr[M] == 0:
#             L = M
#         else:
#             R = M
#
#     if R < n:
#         return R
#     else:
#         return -1
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# result = binary_search_first_one(n, arr)
# print(result)

def binary_search_last_zero(n, arr):
    L = -1
    R = n
    while L + 1 < R:
        M = (L + R) // 2
        if arr[M] == 0:
            L = M
        else:
            R = M

    if L >= 0:
        return L
    else:
        return -1


n = int(input())
arr = list(map(int, input().split()))
result = binary_search_last_zero(n, arr)
print(result)


# INTRODUCTION
# P1. sorted Binary array
# for e.g [000000111111111], find the occurenece of first 1?
# Ans. 1st what we do is naive solution that is linear search , like
# for i=0:n-1
# if(arr[i]==1
# break
# print(i), O(n) - linear search
#
# Searchin Algo:-
# 1. Define Search space:- here is entire array (0 to n-1)
# 2. Navigate the search space and reduce the search space
# 3. Most imp. i.e rule of invarient:-
# something that doesn't change
# like 0000(Block 0)1111(Block1)
# 'L' will always in B0 and 'R' will always in B1
#
# SBA template :-
# L = 0 , R = N-1
# while (L+1 < R){
# M = (L + R )/2
# if A[M]==0 :
# L = M
# else:
# R = M
# So in case of first 1 we have to print R (if(R<N) then print R else "1 does not exist ")
# and in case of last 0 we have to print L( if(L>=0) then print(L) else "0 does not exist ", )
# }
# Q. 000000111111111
# So , L =0, R = 14
# so navigate the seach space and reduce it..
# M = (L + R )/2 = 7
# so at 7 th index i have '1' so now i want to discard right half, so i want to change right i.e
# so R = M, i will not put R = M-1 (as it voilate rule of invarient)
# So , now L = 0 , R = M = 7,
# M = (0+7)/2 = 3
# so at index 3 I have 0 , I need to reduce now left side , So ,
# L = M , L = 3
# M = (3+7)/2 = 5, SO , L=5
# M = (5+7)/2 = 6, So , R  = M = 6,
# L = 5, R = 6, at this point
# while (L+1 < R) we have to exit and print R(first 1 occurenece), i,e 6, log(search space)==> log(N),
#
#
# Some edge cases , If all are 0's :- 0000000000, then ther is noBlock 1, so i will add a dummy '1', now:-
# 00000000001, So I will put L = 0 , R = N instead of R = N-1 (as per SBA template)..
# and also if ask print last 0 then we can print  L,but if case to print 1 we make a condition:-
# if(R<N) then print R else "1 does not exist "
# Other edge case :- is If all are 1's :- 1111111111, then ther is noBlock 0, so i will add a dummy '0', now:-
# 01111111111, So I will put L = -1
# So i print first 1 then R will printed nicely , but if last 0 to print then put a condition if(L>=0) then print(L),  else "0 does not exist ", as in this case we have dummy 0