lines = open("input.txt", "r").read().split("\n")
reports = [list(map(int, x.split())) for x in lines]

safe = 0

for r in reports:
    if r[0] == r[1]:
        continue

    sign = 1 if r[0] < r[1] else -1
    s = True

    for i in range (len(r) - 1):
        x = (r[i + 1] - r[i]) * sign
        if x < 1 or x > 3:
            s = False
            break

    safe += int(s)

print(safe)
