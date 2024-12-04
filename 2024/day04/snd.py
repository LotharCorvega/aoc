grid = open("input.txt", "r").read().split("\n")
n = len(grid)
m = len(grid[0])
count = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        if grid[i][j] != "A":
            continue

        diag1 = "".join(sorted(grid[i-1][j-1] + grid[i+1][j+1]))
        diag2 = "".join(sorted(grid[i-1][j+1] + grid[i+1][j-1]))

        if diag1 == "MS" and diag2 == "MS":
            count += 1

print(count)
