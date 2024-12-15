from collections import deque

grid, moves = open("input.txt", "r").read().strip().split("\n\n")
warehouse = []

expand = { "#": "##", "O": "[]", ".": "..", "@": "@." }

for s in grid.split("\n"):
    line = []
    for c in s:
        line.extend(list(expand[c]))
    warehouse.append(line)

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

    if warehouse[i][j] == "#":
        continue
    elif warehouse[i][j] == ".":
        robot = (i, j)
        continue

    Q = deque([(i, j)])
    V = []

    hit = False

    while len(Q) > 0:
        ui, uj = Q.popleft()

        if (ui, uj) in V:
            continue

        match warehouse[ui][uj]:
            case ".":
                pass
            case "#":
                hit = True
                break
            case "[":
                V.append((ui, uj))
                V.append((ui, uj + 1))

                Q.append((ui + di, uj + dj))
                Q.append((ui + di, uj + dj + 1))
            case "]":
                V.append((ui, uj))
                V.append((ui, uj - 1))

                Q.append((ui + di, uj + dj))
                Q.append((ui + di, uj + dj - 1))

    if hit:
        continue

    for ii, jj in reversed(V):
        tmp = warehouse[ii][jj]
        warehouse[ii][jj] = "."
        warehouse[ii + di][jj + dj] = tmp

    robot = (i, j)

sum = 0

for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "[":
            sum += 100 * i + j

print(sum)
