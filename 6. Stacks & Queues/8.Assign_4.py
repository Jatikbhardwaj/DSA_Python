def largest_rectangle_area(histogram):
    n = len(histogram)
    stack = []
    max_area = 0
    for i in range(n):
        while stack and histogram[i] < histogram[stack[-1]]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] -1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = histogram[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area , height * width)

    return max_area
n = int(input())
histogram = list(map(int,input().split()))

result = largest_rectangle_area(histogram)
print(result )