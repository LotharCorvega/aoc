from itertools import product

lines = open("input.txt", "r").read().strip().split("\n")
sum = 0

for line in lines:
    splt = line.split(":")
    lhs, rhs = int(splt[0]), list(map(int, splt[1].split()))
    n = len(rhs)

    for bits in product((True, False), repeat=(n - 1)):
        x = rhs[0]

        for i in range(1, n):
            if bits[i - 1]:
                x += rhs[i]
            else:
                x *= rhs[i]

            if x > lhs:
                break

        if x == lhs:
            sum += lhs
            break

print(sum)
