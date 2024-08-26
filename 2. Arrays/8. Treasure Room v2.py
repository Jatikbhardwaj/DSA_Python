import sys
import os
import io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def find_blocks(N, W, blocks):
    seen = {}
    for i in range(N - 2):
        for j in range(i + 1, N):
            complement = W - blocks[i] - blocks[j]
            if complement in seen and seen[complement] < i:
                return f"{seen[complement] + 1} {i + 1} {j + 1}\n"
        seen[blocks[i]] = i
    return "-1\n"


N, W = map(int, input().split())
blocks = list(map(int, input().split()))
sys.stdout.write(find_blocks(N, W, blocks))