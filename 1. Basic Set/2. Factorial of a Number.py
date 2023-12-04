def fact(num):
    if num == 0 or num == 1:
      return 1 
    else:
      return num * fact(num-1)
t = int(input())
for i in range(t):
  num = int(input())
  result = fact(num)
  print(result)
  
# Alternative 

def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
t = int(input())
for i in range(t):
   num = int(input())
   result = fact(num)
   print(result)