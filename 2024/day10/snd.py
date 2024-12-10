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
        V = dict()

        Q.append((i, j))
        V[(i, j)] = 1

        while len(Q) > 0:
            u = Q.popleft()

            for (di, dj) in dirs:
                v = (u[0] + di, u[1] + dj)

                if v[0] < 0 or v[0] >= m or v[1] < 0 or v[1] >= n:
                    continue

                hu = int(grid[u[1]][u[0]])
                hv = int(grid[v[1]][v[0]])

                if hv != hu + 1:
                    continue

                if v in V:
                    V[v] += V[u]
                else:
                    V[v] = V[u]
                    Q.append(v)

        for v in V:
            if int(grid[v[1]][v[0]]) == 9:
                score += V[v]

print(score)
