def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * f(n//2) - 1
    else:
        return 2 * f(n//2) + 1

n = int(open("input.txt", "r").read())
print(f(n))