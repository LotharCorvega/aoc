lines = open("input.txt", "r").read().strip().split("\n")
fst, snd = [], []

for line in lines:
    a, b = line.split()
    fst.append(int(a))
    snd.append(int(b))

similarity = 0

for x in fst:
    similarity += snd.count(x) * x

print(similarity)
