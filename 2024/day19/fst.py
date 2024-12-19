from functools import cache

x, y = open("input.txt", "r").read().strip().split("\n\n")
patterns = x.split(", ")
towels = y.split("\n")

@cache
def check(t: str):
    if t == "":
        return True

    for p in patterns:
        if t.startswith(p) and check(t[len(p):]):
            return True
    return False

print(sum(check(t) for t in towels))
