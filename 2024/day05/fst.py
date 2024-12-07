rules_txt, updates_txt = open("input.txt", "r").read().strip().split("\n\n")

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

for u in updates:
    n = len(u)
    ok = True

    for i in range(1, n):
        if not u[i] in after:
            continue

        S = after[u[i]]
        T = set(u[:i])

        if not S.isdisjoint(T):
            ok = False
            break

    if ok:
        sum += u[n // 2]

print(sum)