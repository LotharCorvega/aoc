from functools import cache

x, y = open("input.txt", "r").read().strip().split("\n\n")
patterns = x.split(", ")
towels = y.split("\n")

@cache
def check(t: str):
    if t == "":
        return 1
    s = 0
    for p in patterns:
        if t.startswith(p):
            s += check(t[len(p):])
    return s

print(sum(check(t) for t in towels))
