import re

lines = open("input.txt", "r").read().strip().split("\n")
s = 0

for line in lines:
    m = re.findall(r"mul\((\d+),(\d+)\)", line)
    s += sum(map(lambda x: int(x[0]) * int(x[1]), m))

print(s)
