import re

lines = open("input.txt", "r").read().strip().split("\n")
active = True
s = 0

for line in lines:
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)

    for a, b, do, dont in matches:
        if do:
            active = True
        elif dont:
            active = False
        elif active:
            s += int(a) * int(b)

print(s)
