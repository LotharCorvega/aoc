import re
from z3 import Solver, sat, Int

input = open("input.txt", "r").read().strip().split("\n\n")
machines = []

tokens = 0

for i in input:
    ax, ay, bx, by, px, py = map(int, re.findall(r"(\d+)", i))
    a, b = Int("a"), Int("b")

    S = Solver()
    S.add(a * ax + b * bx == px)
    S.add(a * ay + b * by == py)

    if S.check() == sat:
        m = S.model()
        tokens += m[a].as_long() * 3 + m[b].as_long()

print(tokens)
