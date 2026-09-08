"""Print the first five Fibonacci numbers for the Part D practice run."""


def first_five_fibonacci() -> list[int]:
    values: list[int] = []
    a, b = 0, 1
    for _ in range(5):
        values.append(a)
        a, b = b, a + b
    return values


if __name__ == "__main__":
    print(" ".join(map(str, first_five_fibonacci())))

