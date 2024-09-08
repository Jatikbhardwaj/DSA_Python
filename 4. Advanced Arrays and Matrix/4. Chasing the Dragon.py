def calculate_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum


def min_cost_travel(start, end, n, prefix_sum):
    if start <= end:
        clockwise = prefix_sum[end] - prefix_sum[start]
        anti_clockwise = prefix_sum[n] - clockwise
    else:
        anti_clockwise = prefix_sum[start] - prefix_sum[end]
        clockwise = prefix_sum[n] - anti_clockwise
    return min(clockwise, anti_clockwise)


def solve_dragon_attacks(N, costs, K, attacks):
    prefix_sum = calculate_prefix_sum(costs)

    current_pos = 1
    results = []

    for direction, distance in attacks:
        # Calculate the new position after the dragon's movement
        new_pos = (current_pos + direction * (distance % N) - 1) % N + 1

        # Calculate the minimum cost to travel to the new position
        cost = min_cost_travel(current_pos, new_pos, N, prefix_sum)
        results.append(cost)

        # Update the current position
        current_pos = new_pos

    return results


N = int(input())
costs = list(map(int, input().split()))
K = int(input())
attacks = [tuple(map(int, input().split())) for _ in range(K)]
# N = 5
# costs = [1, 4, 5, 2, 5]
# K= 7
# attacks = [(1, 1), (1, 5), (1, 7), (-1, 4), (-1, 4), (1, 8), (-1, 2)]

results = solve_dragon_attacks(N, costs, K, attacks)
for result in results:
    print(result)

# Time Complexity: The time complexity is O(N + K), where N is the number of cities and K is the number of attacks.
# Space Complexity: O(N) for the prefix sum array.
# Clockwise and Anti-Clockwise Logic in min_cost_travel
#
# The key to understanding this function is recognizing that on a circular path, there are always two ways to travel between two points: clockwise and anti-clockwise. The function aims to find the cheaper of these two options.
#
# if start <= end: This condition checks if the start point is located before the end point when moving along the array indices (which represent positions on the circular path).
#
# clockwise = prefix_sum[end] - prefix_sum[start]: If start is before end, moving from start to end directly using array indices represents clockwise movement. The cost is calculated by subtracting the prefix sum at the start index from the prefix sum at the end index.
# anti_clockwise = prefix_sum[n] - clockwise: The anti-clockwise cost is the total cost of traversing the entire circle (prefix_sum[n]) minus the clockwise cost.
# else (start > end): This block handles cases where the start point comes after the end point in the array indices.
#
# anti_clockwise = prefix_sum[start] - prefix_sum[end]: Here, moving directly from start to end using array indices would mean moving backward, which represents anti-clockwise movement. The cost is calculated similarly to the clockwise cost in the previous case.
# clockwise = prefix_sum[n] - anti_clockwise: The clockwise cost is calculated by subtracting the anti-clockwise cost from the total cost of traversing the circle.

# Modulo Operator (%) for Circular Wrapping
#
# The modulo operator (%) is crucial for simulating movement on a circular path. Here's how it works in the code:
#
# new_pos = (current_pos + direction * (distance % N) - 1) % N + 1
# Let's break this line down step-by-step:
#
# distance % N: This ensures that the distance the dragon travels is always within the bounds of the circular path (0 to N-1). If the distance exceeds the path's length, the modulo operator "wraps" it around. For example, if distance is 7 and N is 5, distance % N would be 2.
#
# direction * (distance % N): This calculates the actual displacement based on the direction. If direction is 1 (clockwise), the displacement is positive. If direction is -1 (anti-clockwise), the displacement is negative.
#
# current_pos + direction * (distance % N): This adds the displacement to the current_pos.
#
# (... - 1) % N + 1:  These adjustments handle the fact that the island positions are numbered from 1 to N, while array indices start from 0. The -1 and +1 ensure the final new_pos falls within the correct range of 1 to N.

# In essence, the modulo operator acts like a circular counter, ensuring that the dragon's position always remains within the bounds of the circular path, no matter how far it travels in either direction.