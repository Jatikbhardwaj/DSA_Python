def count_triplets(points, d):
    n = len(points)
    count = 0

    j = 0

    for i in range(n):

        while j < n and points[j] - points[i] <= d:
            j += 1

        num_points = j - i

        if num_points >= 3:
            count += (num_points - 1) * (num_points - 2) // 2

    return count


n, d = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
result = count_triplets(points, d)

print(result)
