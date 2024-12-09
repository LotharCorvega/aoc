disk = open("input.txt", "r").read().strip()
mem = []

for i in range(len(disk)):
    for _ in range(int(disk[i])):
        if i % 2 == 0:
            mem.append(i//2)
        else:
            mem.append(-1)

i = 0
while True:
    if i >= len(mem):
        break

    if mem[i] != -1:
        i += 1
        continue

    x = mem.pop()

    if x == -1:
        continue

    mem[i] = x

checksum = 0
for i, x in enumerate(mem):
    checksum += i * x

print(checksum)
