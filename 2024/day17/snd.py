from z3 import Optimize, BitVec
import re

def ints(s):
    return list(map(int, re.findall(r"(\d+)", s)))

reg, prog = map(ints, open("input.txt", "r").read().strip().split("\n\n"))
insns = []

for i in range(0, len(prog), 2):
    opcode = prog[i]
    operand = prog[i + 1]

    if operand < 4:
        combo = operand
    else:
        combo = "ABC"[operand - 4]

    match opcode:
        case 0: # adv
            insns.append(f"A = A >> {combo}")
        case 1: # bxl
            insns.append(f"B = B ^ {operand}")
        case 2: # bst
            insns.append(f"B = {combo} % 8")
        case 3: # jnz
            continue # last instruction by magic condition
        case 4: # bxc
            insns.append(f"B = B ^ C")
        case 5: # out
            insns.append(f"out = {combo} % 8")
        case 6: # bdv
            insns.append(f"B = A >> {combo}")
        case 7: # cdv
            insns.append(f"C = A >> {combo}")

code = "\n\t".join(["def f(A):"] + insns)
local_vars = {}

eval(compile(code + "\n\treturn A", "<string>", "exec"), {}, local_vars)
fa = local_vars["f"]
eval(compile(code + "\n\treturn out", "<string>", "exec"), {}, local_vars)
fo = local_vars["f"]

n = len(prog)
A = [BitVec(f"a{i}", 64) for i in range(n + 1)]
O = [BitVec(f"out{i}", 64) for i in range(n)]

opt = Optimize()

opt.add(A[n] == 0)

for i in range(n):
    opt.add(fa(A[i]) == A[i + 1])
    opt.add(fo(A[i]) == O[i])
    opt.add(prog[i]  == O[i])

opt.minimize(A[0])
opt.check()
print(opt.model().eval(A[0]))
