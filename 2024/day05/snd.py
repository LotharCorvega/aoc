from functools import cmp_to_key

rules_txt, updates_txt = open("input.txt", "r").read().split("\n\n")

rules = list(map(lambda x: tuple(map(int, x.split("|"))), rules_txt.split("\n")))
updates = list(map(lambda x: list(map(int, x.split(","))), updates_txt.split("\n")))

after = {}
sum = 0

for r in rules:
    a, b = r
    if not a in after:
        after[a] = {b}
    else:
        after[a].add(b)

def cmp(a, b):
    if a in after and b in after[a]:
        return -1
    else:
        return 0

for u in updates:
    n = len(u)
    uu = sorted(u, key=cmp_to_key(cmp))

    if u != uu:
        sum += uu[n // 2]
        continue

print(sum)