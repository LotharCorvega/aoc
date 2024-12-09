from dataclasses import dataclass

@dataclass
class Block:
    pos: int
    len: int
    id: int

disk = open("input.txt", "r").read().strip()
file, free = [], []
pos = 0

for i in range(len(disk)):
    n = int(disk[i])
    if i % 2 == 0:
        file.append(Block(pos, n, i // 2))
    else:
        free.append(Block(pos, n, -1))
    pos += n

for i in range(len(file) - 1, -1, -1):
    for j in range(len(free)):
        if file[i].pos <= free[j].pos:
            break

        if file[i].len <= free[j].len:
            # freed space
            new_free = Block(file[i].pos, file[i].len, -1)

            # move file
            file[i].pos = free[j].pos

            # insert keeping order (use binary search)
            k = len(free) -1
            while k > 0 and new_free.pos < free[k].pos:
                k -= 1
            free.insert(k, new_free)

            # merge back
            if k < len(free) - 1 and free[k + 1].pos == free[k].pos + free[k].len:
                free[k].len += free[k + 1].len
                free.pop(k + 1)

            # merge front
            if k > 0 and free[j].pos == free[k - 1].pos + free[k - 1].len:
                free[k - 1].len += free[k].len
                free.pop(k)

            # allocate space
            if file[i].len == free[j].len:
                free.pop(j)
            else:
                free[j].pos += file[i].len
                free[j].len -= file[i].len

            break

checksum = 0
for f in file:
    for i in range(f.pos, f.pos + f.len):
        checksum += i * f.id

print(checksum)
