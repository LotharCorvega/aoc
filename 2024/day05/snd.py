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

def resolve(u):
    for i in range(1, len(u)):
        if u[i] not in after:
            continue

        for j in range(i):
            if u[j] in after[u[i]]:
                uu = u[:j] + u[j+1:i+1] + [u[j]] + u[i+1:]
                return True, uu

    return False, []

for u in updates:
    n = len(u)
    incorrectly, _ = resolve(u)

    while incorrectly:
        c, uu = resolve(u)
        if c:
            u = uu
        else:
            sum += u[n // 2]
            break

print(sum)