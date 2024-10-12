def tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append((1, source, destination))
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)

    moves.append((n, source, destination))

    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)


n = int(input())
moves = []
tower_of_hanoi(n, 1, 2, 3, moves)

for move in moves:
    print(move[0], move[1], move[2])
