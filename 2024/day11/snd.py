from functools import cache

stones = list(map(int, open("input.txt", "r").read().strip().split()))

@cache
def sim(n, steps):
    if steps == 0:
        return 1

    ns = str(n)

    if n == 0:
        return sim(1, steps - 1)
    elif len(ns) % 2 == 0:
        fst = int(ns[:len(ns)//2])
        snd = int(ns[len(ns)//2:])
        return sim(fst, steps - 1) + sim(snd, steps - 1)
    else:
        return sim(n * 2024, steps - 1)

print(sum(map(lambda x: sim(x, 75), stones)))
