# Input
# Two integers on the first line, N W.
# N integers on the second line where the i-th integer is li.
# i/p:- 
# 7 8
# 7 5 3 6 9 2 9
# Output
# Any two distinct integers i and j such that li+lj=W. If it is impossible, output −1
# o/p:-2 3

n1, n2 = map(int,input().split())
arr = list(map(int,input().split()))
resultant_dict = {}
index = 1
for num in arr:
    complement = n2 - num
    if complement in resultant_dict:
        print(resultant_dict[complement], index)
        break
    resultant_dict[num] = index
    index += 1
else:
    print("-1")
