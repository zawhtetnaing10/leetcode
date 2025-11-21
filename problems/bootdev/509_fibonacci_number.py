def fib_poly(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    grandparent = 0
    parent = 1
    current = 1

    for _ in range(1, n):
        current = grandparent + parent
        grandparent = parent
        parent = current

    return current


def fib_exp(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_exp(n-2) + fib_exp(n-1)


print(f"{fib_poly(5)}")
print(f"{fib_poly(55)}")

print(f"{fib_exp(5)}")
print(f"{fib_exp(6)}")
