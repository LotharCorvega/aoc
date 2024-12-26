from collections import deque

grid = open("input.txt", "r").read().strip().split("\n")
m, n = len(grid), len(grid[0])

Ei, Ej = next((i, row.index("E")) for i, row in enumerate(grid) if "E" in row)

Q = deque()
D = {}

Q.append((Ei, Ej))
D[(Ei, Ej)] = 0

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while len(Q) > 0:
    i, j = Q.popleft()

    for di, dj, in dirs:
        ii, jj = i + di, j + dj

        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != "#":
            if not (ii, jj) in D or D[(ii, jj)] > D[(i, j)] + 1:
                Q.append((ii, jj))
                D[(ii, jj)] = D[(i, j)] + 1

skips = []
s = 20

for d in range(s + 1):
    for x in range(-d, d + 1):
        y = d - abs(x)
        skips.append((x, y))
        if y != 0:
            skips.append((x, -y))

sum = 0

for i in range(m):
    for j in range(n):
        if not (i, j) in D:
            continue

        for di, dj in skips:
            ii, jj = i + di, j + dj
            ss = abs(di) + abs(dj)

            if (ii, jj) in D and D[(i, j)] - ss >= D[((ii, jj))] + 100:
                sum += 1

print(sum)
