import re

def tran(grid):
    n = len(grid)
    m = len(grid[0])

    cols = []

    for col in range(n):
        cols.append("".join([grid[i][col] for i in range(m)]))

    return cols

def diag(grid, dir):
    n = len(grid)
    m = len(grid[0])

    diags = {}
    for row in range(n):
        for col in range(m):
            key = row + col * dir
            if key not in diags:
                diags[key] = ""
            diags[key] += (grid[row][col])

    return list(diags.values())

grid = open("input.txt", "r").read().split("\n")
all = grid + tran(grid) + diag(grid, -1) + diag(grid, 1)
count = 0

for s in all:
    count += len(re.findall(r"XMAS", s))
    count += len(re.findall(r"XMAS", s[::-1]))

print(count)
