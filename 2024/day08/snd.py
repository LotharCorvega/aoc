from itertools import combinations

lines = open("input.txt", "r").read().strip().split("\n")
m, n = len(lines), len(lines[0])

antennas = {}

for i, line in enumerate(lines):
    for j in range(len(line)):
        if line[j] != ".":
            if line[j] in antennas:
                antennas[line[j]].add((j, i))
            else:
                antennas[line[j]] = {(j, i)}

antinodes = set()

for freq in antennas:
    for p1, p2 in combinations(antennas[freq], 2):
        dx, dy = p1[0] - p2[0], p1[1] - p2[1]

        i = 0
        while True:
            p11 = (p1[0] + i * dx, p1[1] + i * dy)
            if p11[0] >= 0 and p11[0] < n and p11[1] >= 0 and p11[1] < m:
                antinodes.add(p11)
                i += 1
            else:
                break

        j = 0
        while True:
            p22 = (p2[0] - j * dx, p2[1] - j * dy)
            if p22[0] >= 0 and p22[0] < n and p22[1] >= 0 and p22[1] < m:
                antinodes.add(p22)
                j += 1
            else:
                break

print(len(antinodes))
