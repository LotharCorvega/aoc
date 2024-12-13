import re

input = open("input.txt", "r").read().strip().split("\n\n")
tokens = 0

for i in input:    
    a, c, b, d, x, y = map(int, re.findall(r"(\d+)", i))

    A = (d * x + -b * y) // (a * d - b * c)
    B = (-c * x + a * y) // (a * d - b * c)

    if a * A + b * B == x and c * A + d * B == y:
        tokens += A * 3 + B

print(tokens)