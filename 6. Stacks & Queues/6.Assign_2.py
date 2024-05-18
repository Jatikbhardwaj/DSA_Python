def previousGreator(heights):
  n = len(heights)
  stack = []
  result = [-1] * n
  
  for i in range(n):
    while stack and heights[stack[-1]] <= heights[i]:
      stack.pop()
    if stack:
      result[i] = heights[stack[-1]]
    stack.append(i)
    
  return result

i = int(input())  
heights = list(map(int,input().split()))
result = print(*previousGreator(heights))