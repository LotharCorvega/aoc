from collections import deque

bytes = list(map(lambda x: tuple(map(int, x.split(","))), open("input.txt", "r").read().strip().split("\n")))
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
n = 70

Q = deque()
D = {}

Q.append((0, 0))
D[(0, 0)] = 0
block = set(bytes[:1024])

while len(Q) > 0:
    i, j = Q.popleft()
    d = D[(i, j)]

    for di, dj in dirs:
        ii, jj = i + di, j + dj

        if 0 <= ii <= n and 0 <= jj <= n and not (ii, jj) in block:
            if not (ii, jj) in D or D[(ii, jj)] > d + 1:
                D[(ii, jj)] = d + 1
                Q.append((ii, jj))

print(D[(n, n)])
