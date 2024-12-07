lines = open("input.txt", "r").read().strip().split("\n")
fst, snd = [], []

for line in lines:
    a, b = line.split()
    fst.append(int(a))
    snd.append(int(b))

fst = sorted(fst)
snd = sorted(snd)

diff = 0

for i in range(len(fst)):
    diff += abs(fst[i] - snd[i])

print(diff)
