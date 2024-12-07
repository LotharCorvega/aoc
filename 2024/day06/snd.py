grid = open("input.txt", "r").read().strip().split("\n")
m, n = len(grid), len(grid[0])

x, y = next((s.index("^"), i) for i, s in enumerate(grid) if "^" in s)
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def walk(obstruction):
    xc, yc, d = x, y, 0
    visited = {(xc, yc, d)}

    while True:
        xx, yy = xc + dirs[d][0], yc + dirs[d][1]

        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            return False, visited

        if obstruction == (xx, yy) or grid[yy][xx] == "#":
            d = (d + 1) % 4
            continue

        if (xx, yy, d) in visited:
            return True, visited

        xc, yc = xx, yy
        visited.add((xc, yc, d))

path = {p[:2] for p in walk(None)[1]}
print(sum(walk(p[:2])[0] for p in path))
