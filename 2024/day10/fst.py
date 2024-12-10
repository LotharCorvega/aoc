from collections import deque

grid = open("input.txt", "r").read().strip().split("\n")
m, n = len(grid), len(grid[0])
score = 0

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i in range(n):
    for j in range(m):
        if int(grid[j][i]) != 0:
            continue

        Q = deque()
        V = set()

        Q.append((i, j))
        V.add((i, j))

        while len(Q) > 0:
            u = Q.popleft()

            for (di, dj) in dirs:
                v = (u[0] + di, u[1] + dj)

                if v[0] < 0 or v[0] >= m or v[1] < 0 or v[1] >= n:
                    continue

                hu = int(grid[u[1]][u[0]])
                hv = int(grid[v[1]][v[0]])

                if v in V or hv != hu + 1:
                    continue

                Q.append(v)
                V.add(v)

        for v in V:
            if int(grid[v[1]][v[0]]) == 9:
                score += 1

print(score)
