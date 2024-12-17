import re

def ints(s):
    return list(map(int, re.findall(r"(\d+)", s)))

reg, prog = map(ints, open("input.txt", "r").read().strip().split("\n\n"))
out = []
ip = 0

while ip < len(prog):
    opcode = prog[ip]
    operand = prog[ip + 1]

    if operand < 4:
        combo = operand
    else:
        combo = reg[operand - 4]

    match opcode:
        case 0: # adv
            reg[0] = reg[0] // (2**combo)
        case 1: # bxl
            reg[1] = reg[1] ^ operand
        case 2: # bst
            reg[1] = combo % 8
        case 3: # jnz
            if reg[0] != 0:
                ip = operand
                continue
        case 4: # bxc
            reg[1] = reg[1] ^ reg[2]
        case 5: # out
            out.append(combo % 8)
        case 6: # bdv
            reg[1] = reg[0] // (2**combo)
        case 7: # cdv
            reg[2] = reg[0] // (2**combo)

    ip += 2

print(",".join(map(str, out)))
