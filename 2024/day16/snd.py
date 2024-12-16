from collections import deque

grid = list(map(list, open("input.txt", "r").read().strip().split("\n")))
Si, Sj = next((i, row.index("S")) for i, row in enumerate(grid) if "S" in row)

Q = deque()
D = {}
P = {}

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
        P[nxt] = {u}
    elif D[nxt] == c + 1000:
        Q.append(nxt)
        D[nxt] = c + 1000
        P[nxt].add(u)

    # rotate right
    nxt = (i, j, (d + 1) % 4)
    if not nxt in D or D[nxt] > c + 1000:
        Q.append(nxt)
        D[nxt] = c + 1000
        P[nxt] = {u}
    elif D[nxt] == c + 1000:
        Q.append(nxt)
        D[nxt] = c + 1000
        P[nxt].add(u)

    # move
    ii, jj = i + dirs[d][0], j + dirs[d][1]
    nxt = (ii, jj, d)
    if grid[ii][jj] != "#":
        if not nxt in D or D[nxt] > c + 1:
            Q.append(nxt)
            D[nxt] = c + 1
            P[nxt] = {u}
        elif D[nxt] == c + 1:
            Q.append(nxt)
            D[nxt] = c + 1
            P[nxt].add(u)

Ei, Ej = next((i, row.index("E")) for i, row in enumerate(grid) if "E" in row)
d = min(range(4), key=lambda d: D[(Ei, Ej, d)])

Q = deque()
S = set()

Q.append((Ei, Ej, d))
S.add((Ei, Ej, d))

while len(Q) > 0:
    u = Q.popleft()

    if not u in P:
        continue

    for v in P[u]:
        S.add(v[:2])
        Q.append(v)

print(len(S))
