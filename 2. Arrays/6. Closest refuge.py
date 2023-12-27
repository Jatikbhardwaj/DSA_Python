n = int(input())         # 3
array = list(map(int,input().split()))  # 2 4 3  
my_dict = {i: False for i in range(1, n + 2)}  # 1:False, 2: False , 3:False
# my_dict = {}
for i in range(n):                       # i = 0, 1, 2
    if array[i] >= 1 and array[i] <= n:   
        my_dict[array[i]] = True     # 1:False , 2:true, 3:False
for j in range(1, n + 2):
    if my_dict[j] == False:
        break
print(my_dict)
print(j)

