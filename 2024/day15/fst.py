grid, moves = open("input.txt", "r").read().strip().split("\n\n")
warehouse = list(map(list, grid.split("\n")))

for i, row in enumerate(warehouse):
    if "@" in row:
        j = row.index("@")
        warehouse[i][j] = "."
        robot = (i, j)
        break

dirs = { "^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1) }

for m in moves.replace("\n", ""):
    di, dj = dirs[m]
    i, j = robot[0] + di, robot[1] + dj

    match warehouse[i][j]:
        case "#":
            pass
        case ".":
            robot = (i, j)
        case "O":
            n = 2
            while True:
                ii, jj = robot[0] + n * di, robot[1] + n * dj
                n += 1
                if warehouse[ii][jj] != "O":
                    break

            if warehouse[ii][jj] == ".":
                robot = (i, j)
                warehouse[i][j] = "."
                warehouse[ii][jj] = "O"

sum = 0

for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "O":
            sum += 100 * i + j

print(sum)
