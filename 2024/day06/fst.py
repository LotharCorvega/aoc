grid = open("input.txt", "r").read().split("\n")
m, n = len(grid), len(grid[0])

x, y = next((s.index("^"), i) for i, s in enumerate(grid) if "^" in s)
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

visited = {(x, y)}
d = 0

while True:
    xx, yy = x + dirs[d][0], y + dirs[d][1]

    if xx < 0 or xx >= n or yy < 0 or yy >= m:
        break

    if grid[yy][xx] == "#":
        d = (d + 1) % 4
        continue

    x, y = xx, yy
    visited.add((x, y))

print(len(visited))
