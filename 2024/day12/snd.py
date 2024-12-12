garden = open("input.txt", "r").read().strip().split("\n")
m, n = len(garden), len(garden[0])

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def fill(p, c):
    Q = [p]
    V = {p}

    while len(Q) > 0:
        u = Q.pop()

        for (di, dj) in dirs:
            v = (u[0] + di, u[1] + dj)

            if v in V or not (0 <= v[0] < m and 0 <= v[1] < n) or garden[v[0]][v[1]] != c:
                continue

            Q.append(v)
            V.add(v)

    return V

def border(p):
    b = 0

    for u in p:
        for (di, dj) in dirs:
            v = (u[0] + di, u[1] + dj)

            if not v in p:
                b += 1

    return b

patterns = {
    (True, True, False, False),
    (False, False, True, True),
    (True, False, True, False),
    (False, True, False, True)
}

def merges(p):
    min_i = min(map(lambda x: x[0], p)) - 1
    max_i = max(map(lambda x: x[0], p)) + 1
    min_j = min(map(lambda x: x[1], p)) - 1
    max_j = max(map(lambda x: x[1], p)) + 1

    merges = 0

    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            x = (
                (i + 0, j + 0) in p,
                (i + 0, j + 1) in p,
                (i + 1, j + 0) in p,
                (i + 1, j + 1) in p
            )

            merges += x in patterns

    return merges

visited = set()
sum = 0

for i in range(m):
    for j in range(n):
        if not (i, j) in visited:
            plot = fill((i, j), garden[i][j])
            bord = border(plot)
            mrgs = merges(plot)

            visited.update(plot)
            sum += len(plot) * (bord - mrgs)

print(sum)
