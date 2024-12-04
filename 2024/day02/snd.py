lines = open("input.txt", "r").read().split("\n")
reports = [list(map(int, x.split())) for x in lines]

safe = 0

for r in reports:
    for sign in [-1, 1]:
        wild = 0
        i = 0

        while i < len(r) - 1:
            x = (r[i + 1] - r[i]) * sign
            if x < 1 or x > 3:
                if i == len(r) - 2:
                    wild += 1
                    break

                xx = (r[i + 2] - r[i]) * sign
                if xx < 1 or xx > 3:
                    if i == 0:
                        xxx = (r[2] - r[1]) * sign

                        if xxx < 1 or xxx > 3:
                            wild += 999
                            break
                        else:
                            wild += 1
                            i += 1
                            continue

                    wild += 999
                    break
                else:
                    wild += 1
                    i += 2
                    continue

            if wild > 1:
                break

            i += 1

        if wild <= 1:
            safe += 1
            break

print(safe)
