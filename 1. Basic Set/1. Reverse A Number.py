t = int(input())
for i in range(t):
    num = int(input())
    reverse = 0
    while (num):
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    print(reverse)

# Alternative method

t = int(input())
for i in range(t):
    num = int(input())
    reverse = int(str(num)[::-1])
    print(reverse)
