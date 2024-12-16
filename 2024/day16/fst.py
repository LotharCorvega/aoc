from collections import deque

grid = list(map(list, open("input.txt", "r").read().strip().split("\n")))
Si, Sj = next((i, row.index("S")) for i, row in enumerate(grid) if "S" in row)

Q = deque()
D = {}

Q.append((Si, Sj, 0))
D[(Si, Sj, 0)] = 0

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while len(Q) > 0:
    u = Q.popleft()
    (i, j, d), c = u, D[u]

    # rotate left
    nxt = (i, j, (d - 1) % 4)
    if not nxt in D or D[nxt] > c + 1000:
        Q.append(nxt)
        D[nxt] = c + 1000

    # rotate right
    nxt = (i, j, (d + 1) % 4)
    if not nxt in D or D[nxt] > c + 1000:
        Q.append(nxt)
        D[nxt] = c + 1000

    # move
    ii, jj = i + dirs[d][0], j + dirs[d][1]
    nxt = (ii, jj, d)
    if grid[ii][jj] != "#" and (not nxt in D or D[nxt] > c + 1):
        Q.append(nxt)
        D[nxt] = c + 1

Ei, Ej = next((i, row.index("E")) for i, row in enumerate(grid) if "E" in row)
print(min([D[(Ei, Ej, d)] for d in range(4)]))
